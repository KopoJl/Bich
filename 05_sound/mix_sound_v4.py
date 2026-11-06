# «03:06» — сведение v4 под монтаж v2 (07_montage/edl.py → work_v2/timeline.json).
# Все события привязаны к времени ВНУТРИ дубля: (клип, t_дубля). Если момент вырезан монтажом — событие пропускается.
# Правила жанра — как в v3 (см. 05_sound/sound_design.md) + J/L-склейки: подложки идут сквозь склейки.
import subprocess, struct, re, json, os
S = "sfx"; VID = "../07_montage/edit_v2_video.mp4"; OUT = "../07_montage/0306_edit_v2.mp4"
TL = json.load(open("../07_montage/work_v2/timeline.json")); CL = {c["id"]: c for c in TL["clips"]}; TOTAL = TL["total"]
TMP = "/tmp/claude-0/-home-user-Bich/939377ca-f5da-57b2-867a-fc6105a9df4e/scratchpad/mix_v4.wav"
FILES = {"SH010":"SH010_take1","SH020":"SH020_take2","SH030":"SH030_take2","SH040a":"SH040_take1","SH040b":"SH040_take1",
 "SH050":"SH050_take1","SH060":"SH060_take3","SH070":"SH070_take3","SH080":"SH080_take2","SH090":"SH090_take1",
 "SH100a":"SH100_take1","SH100b":"SH100_take1","SH100c":"SH100_take1","SLIP1":"SH100a_take1","SLIP2":"SH100a_take1",
 "SH110a":"SH110a_take1","SH110b":"SH110b_take1","SH115":"SH115_take1","SH120":"SH120_take1","SH125":"SH125_take1",
 "SH130":"SH130_take1","SH135":"SH135_take1","SH140":"SH140_take1"}
DIALOG = {"SH010","SH030","SH060"}

def T(cid, local=None, off=0.0):
    """Время на монтаже: local — время внутри дубля; None — начало клипа; 'end' — конец клипа."""
    c = CL[cid]
    if local is None: return c["t0"] + off
    if local == "end": return c["t0"] + (c["out"] - c["in"]) + off
    if not (c["in"] - 1e-3 <= local <= c["out"] + 1e-3): return None
    return c["t0"] + (local - c["in"]) + off

def run(c): return subprocess.run(c, capture_output=True, text=True)
def lufs(p):
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", run(["ffmpeg","-hide_banner","-i",p,"-af","ebur128","-f","null","-"]).stderr)
    return float(m[-1]) if m else -20.0
def peak(p):
    m = re.search(r"max_volume: (-?[\d.]+) dB", run(["ffmpeg","-hide_banner","-i",p,"-af","volumedetect","-f","null","-"]).stderr)
    return float(m.group(1)) if m else 0.0
def onset(p, thr_db=30):
    raw = subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout
    s = struct.unpack("<%dh" % (len(raw)//2), raw); pk = max(1, max(abs(x) for x in s)); th = pk*10**(-thr_db/20)
    for i, x in enumerate(s):
        if abs(x) >= th: return max(0.0, i/8000 - 0.01)
    return 0.0

WIN = "highpass=f=120,lowpass=f=2800"; HALL = "aecho=0.8:0.5:35|70:0.22|0.12"
CLK = "atrim=0:0.35,afade=t=out:st=0.2:d=0.15"
TAPE = "highpass=f=300,lowpass=f=3200,acompressor"
# ---- подложки: (начало, конец, файл, цель LUFS, fade_in, fade_out, группа, фильтр)
BEDS = [
 (0.0,               T("SH020"),            "rain_bed.mp3", -30, 1.0, 0.0, "AMB", WIN),
 (T("SH020"),        T("SH080",2.0),        "rain_bed.mp3", -36, 0.0, 0.15,"AMB", WIN),
 (T("SH050",None,-0.3), T("SH080",2.0),     "room_tone.mp3",-42, 1.0, 0.15,"AMB", ""),
 (T("SH050",None,-0.3), T("SH080",2.0),     "drone.mp3",    -34, 6.0, 0.10,"MUS", "lowpass=f=400"),
 (T("SH090"),        T("SH130",4.25),       "drone.mp3",    -28, 0.05,0.02,"MUS", "lowpass=f=400"),
 (T("SH100a"),       T("SH115","end"),      "room_tone.mp3",-44, 0.2, 0.3, "AMB", HALL),
 (T("SH120"),        T("SH130",4.25),       "room_tone.mp3",-42, 0.3, 0.02,"AMB", ""),
 (T("SH010"),        T("SH010","end"),      "motor_hiss.mp3",-38,0.2, 0.2, "FX", ""),
 (T("SH060"),        T("SH060","end"),      "motor_hiss.mp3",-40,0.1, 0.4, "FX", ""),
 (T("SH120"),        T("SH130",4.25),       "motor_hiss.mp3",-38,0.4, 0.02,"FX", ""),
 (T("SH115"),        T("SH130"),            "heartbeat.mp3",-30, 2.0, 0.3, "MUS", "lowpass=f=200"),
 (T("SH130",4.25,-3.6), T("SH130",4.25),    "riser.mp3",    -26, 0.5, 0.02,"MUS", ""),
 (T("SH135"),        T("SH135",0.5,4.0),    "rain_bed.mp3", -38, 2.0, 2.0, "AMB", WIN),
 (T("SH135"),        T("SH135",0.5,4.0),    "room_tone.mp3",-44, 1.0, 1.5, "AMB", ""),
 (T("SH140",None,-1.5), T("SH140","end"),   "morning_amb.mp3",-32,2.0,0.02,"AMB", "highpass=f=150"),
]
# ---- события: (время, файл, dB от пика -1 dBFS, панорама, фильтр, по атаке, группа)
EV = [
 (T("SH010",5.50),"stop_clack.mp3",-10,0,CLK,True,"FX"),
 (T("SH020",1.90),"teacup_clink.mp3",-16,0,"",True,"FX"),
 (T("SH020",2.00),"bus_night.mp3",-20,0.5,"lowpass=f=1800",False,"FX"),
 (T("SH020",5.00),"creak_upstairs.mp3",-12,0,"lowpass=f=2500",True,"FX"),
 (T("SH030",1.40),"creak_stair.mp3",-13,-0.4,"lowpass=f=2200",True,"FX"),
 (T("SH040a",1.60),"relay_click.mp3",-10,0,CLK,True,"FX"),
 (T("SH050"),"cupboard_drips.mp3",-22,0.7,"",False,"FX"),
 (T("SH050",4.40),"tape_rewind.mp3",-18,0,"atrim=0:0.5,afade=t=out:st=0.3:d=0.2",False,"FX"),   # J-cut: перемотка обрывается PLAY
 (T("SH060"),"play_clack.mp3",-8,0,CLK,True,"FX"),
 (T("SH070",0.80),"needle_drop.mp3",-12,-0.6,"",True,"FX"),
 (T("SH070",0.95),"music_box.mp3",-20,-0.6,"lowpass=f=4000",False,"MUS"),
 (T("SH070",2.65),"torch_grab.mp3",-14,0,"",True,"FX"),
 (T("SH070",4.85),"chair_creak.mp3",-14,0,"",True,"FX"),
 (T("SH080",0.55),"lamp_click.mp3",-12,-0.3,CLK,True,"FX"),
 (T("SH080",1.15),"cupboard_drips.mp3",-20,0,"afade=t=out:st=0.6:d=0.25",False,"FX"),
 (T("SH080",4.20),"torch_click.mp3",-12,-0.3,CLK,True,"FX"),
 (T("SH080",4.65),"torch_click.mp3",-12,-0.3,CLK,True,"FX"),
 (T("SH080",5.25),"torch_click.mp3",-11,-0.3,CLK,True,"FX"),
 (T("BLINK1"),"torch_rattle.mp3",-14,0,"",True,"FX"),
 (T("SH090"),"violin_stab.mp3",-6,0,"",True,"MUS"),
 (T("SH090"),"coat_drips.mp3",-22,0,"",False,"FX"),
 (T("SH100a"),"run_hall.mp3",-10,0,HALL+",afade=t=out:st=5.4:d=0.3",False,"FX"),
 (T("SH100a",1.30),"wall_knocks.mp3",-20,-0.7,"lowpass=f=900",False,"FX"),
 (T("SH100b",2.70),"wall_knocks.mp3",-21,0.7,"lowpass=f=900",False,"FX"),
 (T("SLIP1",0.40),"slipper_drop.mp3",-12,0,HALL,True,"FX"),
 (T("SH100b",3.20),"small_door.mp3",-10,0.3,HALL,True,"FX"),
 (T("SH100c",4.40),"torch_rattle.mp3",-12,0,"",True,"FX"),
 (T("SH100c",4.90),"torch_rattle.mp3",-12,0,"",True,"FX"),
 (T("SH110a",0.40),"fuse_clunk.mp3",-8,0.4,HALL,True,"FX"),
 (T("SH110a",0.85),"fuse_clunk.mp3",-9,0.4,HALL,True,"FX"),
 (T("SH110a",1.25),"fuse_clunk.mp3",-8,0.4,HALL,True,"FX"),
 (T("SH110a",1.60),"ruth_voice_306.wav",-8,0,TAPE+",aecho=0.8:0.7:60:0.3,lowpass=f=1800",False,"VOICE"),
 (T("SH110a",3.70),"whoosh.mp3",-10,0,"",True,"FX"),
 (T("SH110b"),"low_strings.mp3",-5,0,"",True,"MUS"),
 (T("SH110b"),"coat_drips.mp3",-22,0,HALL,False,"FX"),
 (T("BLINK2"),"torch_rattle.mp3",-12,0,"",True,"FX"),
 (T("SH115"),"steps_sock.mp3",-14,0,HALL,False,"FX"),
 (T("BLINK2"),"ruth_voice_full.wav",-10,0,TAPE+",aecho=0.8:0.6:40:0.25",False,"VOICE"),          # J-cut: голос раньше картинки
 (T("SH120",0.40),"ruth_voice_full.wav",-8,0,"highpass=f=250,lowpass=f=3000,acompressor,asetrate=48000*0.8,aresample=48000",False,"VOICE"),
 (T("SH120",1.80),"steps_sock.mp3",-20,-0.3,"",False,"FX"),
 (T("SH120"),"coat_drips.mp3",-22,0.2,"",False,"FX"),
 (T("SH125",1.20),"ruth_voice_full.wav",-6,0,"highpass=f=200,lowpass=f=2600,acompressor,asetrate=48000*0.6,aresample=48000,aecho=0.8:0.5:80:0.3",False,"VOICE"),
 (T("SH125",1.20),"scared_breath.mp3",-18,0,"",False,"FX"),
 (T("SH125",3.45),"torch_drop.mp3",-12,0,"",True,"FX"),
 (T("SH130",0.83),"eject.mp3",-10,0,"",True,"FX"),
 (T("SH130",2.13),"tape_pull.mp3",-13,0,"",False,"FX"),
 (T("SH130",4.25),"tape_snap.mp3",-5,0,"",True,"FX"),
 (T("SH130",4.90),"recorder_drop.mp3",-11,0,"",True,"FX"),
 (T("SH135",1.10),"scared_breath.mp3",-20,0,"",False,"FX"),
 (T("SH135",2.70),"bus_night.mp3",-28,0.6,"lowpass=f=1200",False,"FX"),
 (T("SH140",0.25),"bus_morning.mp3",-18,0,"lowpass=f=3000",False,"FX"),
 (T("SH140",0.0),"sleep_breath.mp3",-24,-0.2,"",False,"FX"),
 (T("SH140",5.60),"relay_click.mp3",-8,0,CLK,True,"FX"),
]
# ---- тишина: звук генераций в ноль
MUTE = [(T("SH080",2.0), T("SH090")), (T("BLACK2"), T("SH110a")), (T("SH130",4.25), T("SH135")), (T("BLACK3"), TOTAL)]

inputs, fl, groups, k = [], [], {"VOICE":[], "AMB":[], "FX":[], "MUS":[]}, 0
# звук генераций: каждый клип из своего дубля, реплики громко, остальное -22 дБ
orig = []
for c in TL["clips"]:
    if c["id"] not in FILES: continue
    f = f"../06_takes/{FILES[c['id']]}.mp4"; g = 0 if c["id"] in DIALOG else -22
    inputs += ["-ss", f"{c['in']}", "-to", f"{c['out']}", "-i", f]
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,volume={g-4}dB,"
              f"afade=t=in:d=0.02,afade=t=out:st={max(0,c['out']-c['in']-0.03):.3f}:d=0.03,adelay={int(c['t0']*1000)}:all=1[o{k}]")
    orig.append(f"[o{k}]"); k += 1
mu = "+".join(f"between(t,{a:.3f},{b:.3f})" for a, b in MUTE)
fl.append("".join(orig) + f"amix=inputs={len(orig)}:normalize=0:duration=longest,volume='if({mu},0,1)':eval=frame[orig]")
fl.append("[orig]asplit=2[origmix][origkey]"); groups["VOICE"].append("[origmix]")
for a, b, f, tgt, fi, fo, g, filt in BEDS:
    p = f"{S}/{f}"; gain = tgt - lufs(p); d = b - a
    inputs += ["-stream_loop","-1","-i",p]
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo" + (f",{filt}" if filt else "") +
              f",atrim=0:{d:.3f},asetpts=N/SR/TB,volume={gain:.1f}dB,afade=t=in:d={fi},afade=t=out:st={max(0,d-fo):.3f}:d={fo},"
              f"adelay={int(a*1000)}:all=1[x{k}]")
    groups[g].append(f"[x{k}]"); k += 1
for t, f, db, pan, filt, al, g in EV:
    if t is None: continue
    p = f"{S}/{f}"; gain = -1 - peak(p) + db; st = max(0.0, t - (onset(p) if al else 0.0))
    lg, rg = min(1.0, 1-pan), min(1.0, 1+pan)
    inputs += ["-i", p]
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,volume={gain:.1f}dB" + (f",{filt}" if filt else "") +
              f",aformat=channel_layouts=mono,pan=stereo|c0={lg:.2f}*c0|c1={rg:.2f}*c0,adelay={int(st*1000)}:all=1[x{k}]")
    groups[g].append(f"[x{k}]"); k += 1
def bus(n, labs): fl.append("".join(labs) + f"amix=inputs={len(labs)}:normalize=0:duration=longest[{n}]")
bus("voice", groups["VOICE"]); fl.append("[voice]asplit=2[voiceout][vk]")
fl.append("[vk][origkey]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo[key]")
bus("amb0", groups["AMB"]); bus("fx", groups["FX"]); bus("mus", groups["MUS"])
fl.append("[amb0][key]sidechaincompress=threshold=0.015:ratio=8:attack=15:release=450[amb]")
fl.append(f"[voiceout][amb][fx][mus]amix=inputs=4:normalize=0:duration=longest,atrim=0:{TOTAL:.3f},aformat=sample_fmts=fltp:channel_layouts=stereo[mix]")
open("mix_v4_filter.txt","w").write(";\n".join(fl))
r = run(["ffmpeg","-v","error","-y"] + inputs + ["-filter_complex",";".join(fl),"-map","[mix]","-c:a","pcm_f32le","-ar","48000",TMP])
if r.returncode: print(r.stderr[-3000:]); raise SystemExit(1)
I = lufs(TMP); g = -17.0 - I; print(f"pre-master {I:.1f} LUFS -> {g:+.1f} dB")
r = run(["ffmpeg","-v","error","-y","-i",VID,"-i",TMP,"-filter_complex",f"[1:a]volume={g:.2f}dB,alimiter=limit=0.84:attack=2:release=60,apad[a]",
         "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","256k","-ar","48000","-t",f"{TOTAL:.3f}",OUT])
if r.returncode: print(r.stderr[-2000:]); raise SystemExit(1)
print("ok", OUT, f"final {lufs(OUT):.1f} LUFS")
