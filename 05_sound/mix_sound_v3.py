# «03:06» — сведение v3 (правила жанра).
# 1) Каждый файл нормализуется к эталону: подложки по LUFS, точечные эффекты по пику (-1 dBFS).
# 2) Группы: VOICE (речь из генераций SH010/SH030/SH060 + голос с плёнки), AMB (дождь, тон комнаты, утро),
#    FX (точечные), MUS (гул, сердце, подъём). AMB приседает под VOICE (sidechain).
# 3) Звук генераций вне реплик почти выключен — его заменяют эффекты.
# 4) Тишина перед ударами; громкость — статическим усилением до -17 LUFS, затем лимитер -1.5 dBTP.
import subprocess, struct, re, os
S = "sfx"; CUT = "../07_montage/0306_roughcut_v1.mp4"; OUT = "../07_montage/0306_cut_v3.mp4"
TMP = "/tmp/claude-0/-home-user-Bich/939377ca-f5da-57b2-867a-fc6105a9df4e/scratchpad/mix_v3.wav"
TOTAL = 87.30

def run(c): return subprocess.run(c, capture_output=True, text=True)
def lufs(p):
    e = run(["ffmpeg","-hide_banner","-i",p,"-af","ebur128","-f","null","-"]).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", e); return float(m[-1]) if m else -20.0
def peak(p):
    e = run(["ffmpeg","-hide_banner","-i",p,"-af","volumedetect","-f","null","-"]).stderr
    m = re.search(r"max_volume: (-?[\d.]+) dB", e); return float(m.group(1)) if m else 0.0
def onset(p, thr_db=30):
    raw = subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout
    s = struct.unpack("<%dh" % (len(raw)//2), raw); pk = max(1, max(abs(x) for x in s)); th = pk*10**(-thr_db/20)
    for i, x in enumerate(s):
        if abs(x) >= th: return max(0.0, i/8000 - 0.01)
    return 0.0

# ---- подложки: (файл, начало, конец, цель LUFS, fade_in, fade_out, группа, фильтр)
WIN = "highpass=f=120,lowpass=f=2800"           # дождь «за стеклом»
HALL = "aecho=0.8:0.5:35|70:0.22|0.12"          # узкий коридор
BEDS = [
 ("rain_bed.mp3",   0.00,  6.00, -30, 1.0, 0.0, "AMB", WIN),     # задать место
 ("rain_bed.mp3",   6.00, 42.55, -36, 0.0, 0.2, "AMB", WIN),     # уходит назад
 ("room_tone.mp3", 22.75, 42.55, -42, 2.0, 0.2, "AMB", ""),
 ("drone.mp3",     22.75, 42.55, -34, 8.0, 0.15, "MUS", "lowpass=f=400"),  # 2-й проход: медленно растёт
 # 42.75–46.38 — мёртвая тишина (только щелчки фонарика)
 ("drone.mp3",     46.54, 75.72, -28, 0.05, 0.02, "MUS", "lowpass=f=400"),  # 3-й проход
 ("room_tone.mp3", 48.17, 62.63, -44, 0.3, 0.3, "AMB", HALL),
 ("room_tone.mp3", 62.63, 75.72, -42, 0.3, 0.02, "AMB", ""),
 ("motor_hiss.mp3", 0.00,  6.00, -38, 0.2, 0.3, "FX", ""),
 ("motor_hiss.mp3",28.75, 34.75, -40, 0.1, 0.5, "FX", ""),
 ("motor_hiss.mp3",62.63, 75.72, -38, 0.5, 0.02, "FX", ""),
 ("heartbeat.mp3", 60.43, 71.47, -30, 3.0, 0.4, "MUS", "lowpass=f=200"),  # подход Рут к нему
 ("riser.mp3",     71.72, 75.72, -26, 0.5, 0.02, "MUS", ""),              # обрывается на обрыве ленты
 ("rain_bed.mp3",  77.47, 81.50, -38, 2.0, 2.0, "AMB", WIN),             # звуки дома возвращаются
 ("room_tone.mp3", 77.47, 81.50, -44, 1.0, 1.5, "AMB", ""),
 ("morning_amb.mp3",79.50, 86.30, -32, 2.5, 0.02, "AMB", "highpass=f=150"),
]
# ---- точечные: (время, файл, dB после нормализации пика к -1 dBFS, панорама, фильтр, по атаке, группа)
SPOTS = [
 (5.50,"stop_clack.mp3",-10,0,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (7.90,"teacup_clink.mp3",-16,0,"",True,"FX"),
 (8.00,"bus_night.mp3",-20,0.5,"lowpass=f=1800",False,"FX"),
 (11.00,"creak_upstairs.mp3",-12,0,"lowpass=f=2500",True,"FX"),
 (13.40,"creak_stair.mp3",-13,-0.4,"lowpass=f=2200",True,"FX"),
 (19.60,"relay_click.mp3",-10,0,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (22.75,"cupboard_drips.mp3",-22,0.7,"",False,"FX"),
 (23.30,"teacup_clink.mp3",-20,0,"",True,"FX"),
 (27.70,"tape_rewind.mp3",-16,0,"",False,"FX"),
 (28.75,"play_clack.mp3",-8,0,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (35.55,"needle_drop.mp3",-12,-0.6,"",True,"FX"),
 (35.70,"music_box.mp3",-20,-0.6,"lowpass=f=4000",False,"MUS"),
 (37.40,"torch_grab.mp3",-14,0,"",True,"FX"),
 (39.60,"chair_creak.mp3",-14,0,"",True,"FX"),
 (41.30,"lamp_click.mp3",-12,-0.3,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (41.90,"cupboard_drips.mp3",-20,0,"afade=t=out:st=0.6:d=0.25",False,"FX"),
 (44.95,"torch_click.mp3",-12,-0.3,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (45.40,"torch_click.mp3",-12,-0.3,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (46.00,"torch_click.mp3",-11,-0.3,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
 (46.25,"torch_rattle.mp3",-14,0,"",True,"FX"),
 (46.54,"violin_stab.mp3",-6,0,"",True,"MUS"),
 (46.60,"coat_drips.mp3",-22,0,"",False,"FX"),
 (48.17,"run_hall.mp3",-10,0,HALL+",afade=t=out:st=5.6:d=0.3",False,"FX"),
 (49.50,"wall_knocks.mp3",-20,-0.7,"lowpass=f=900",False,"FX"),
 (50.90,"wall_knocks.mp3",-21,0.7,"lowpass=f=900",False,"FX"),
 (50.30,"slipper_drop.mp3",-12,0,HALL,True,"FX"),
 (52.20,"small_door.mp3",-10,0.3,HALL,True,"FX"),
 (53.00,"torch_rattle.mp3",-12,0,"",True,"FX"),
 (53.35,"torch_rattle.mp3",-12,0,"",True,"FX"),
 (55.00,"fuse_clunk.mp3",-8,0.4,HALL,True,"FX"),
 (55.45,"fuse_clunk.mp3",-9,0.4,HALL,True,"FX"),
 (55.85,"fuse_clunk.mp3",-8,0.4,HALL,True,"FX"),
 (56.23,"ruth_voice_306.wav",-8,0,"highpass=f=300,lowpass=f=3200,acompressor,aecho=0.8:0.7:60:0.3,lowpass=f=1800",False,"VOICE"),
 (58.30,"whoosh.mp3",-10,0,"",True,"FX"),
 (58.63,"low_strings.mp3",-5,0,"",True,"MUS"),
 (58.70,"coat_drips.mp3",-22,0,HALL,False,"FX"),
 (60.30,"torch_rattle.mp3",-12,0,"",True,"FX"),
 (60.43,"steps_sock.mp3",-14,0,HALL,False,"FX"),
 (60.60,"ruth_voice_full.wav",-10,0,"highpass=f=300,lowpass=f=3200,acompressor,aecho=0.8:0.6:40:0.25",False,"VOICE"),
 (63.00,"ruth_voice_full.wav",-8,0,"highpass=f=250,lowpass=f=3000,acompressor,asetrate=48000*0.8,aresample=48000",False,"VOICE"),
 (64.40,"steps_sock.mp3",-20,-0.3,"",False,"FX"),
 (62.70,"coat_drips.mp3",-22,0.2,"",False,"FX"),
 (66.60,"ruth_voice_full.wav",-6,0,"highpass=f=200,lowpass=f=2600,acompressor,asetrate=48000*0.6,aresample=48000,aecho=0.8:0.5:80:0.3",False,"VOICE"),
 (66.47,"scared_breath.mp3",-18,0,"",False,"FX"),
 (69.95,"torch_drop.mp3",-12,0,"",True,"FX"),
 (72.30,"eject.mp3",-10,0,"",True,"FX"),
 (73.60,"tape_pull.mp3",-13,0,"",False,"FX"),
 (75.72,"tape_snap.mp3",-5,0,"",True,"FX"),
 (76.37,"recorder_drop.mp3",-11,0,"",True,"FX"),
 (77.60,"scared_breath.mp3",-20,0,"",False,"FX"),
 (79.20,"bus_night.mp3",-28,0.6,"lowpass=f=1200",False,"FX"),
 (80.60,"bus_morning.mp3",-18,0,"lowpass=f=3000",False,"FX"),
 (80.50,"sleep_breath.mp3",-24,-0.2,"",False,"FX"),
 (86.07,"relay_click.mp3",-8,0,"atrim=0:0.35,afade=t=out:st=0.2:d=0.15",True,"FX"),
]
# ---- звук генераций: реплики громко, остальное почти выключено, тишина — в ноль
DIALOG = [(0,6.0),(12.0,18.0),(28.75,34.75)]
MUTE = [(42.75,46.38),(54.33,54.63),(75.72,77.47),(86.30,TOTAL)]  # реле 86.07 звучит уже в чёрном

inputs = ["-i", CUT]; fl = []; groups = {"VOICE":[], "AMB":[], "FX":[], "MUS":[]}
dl = "+".join(f"between(t,{a},{b})" for a,b in DIALOG); mu = "+".join(f"between(t,{a},{b})" for a,b in MUTE)
fl.append(f"[0:a]aresample=48000,highpass=f=80,volume='if({mu},0,if({dl},1.0,0.08))':eval=frame,volume=-4dB[orig]")
fl.append("[orig]asplit=2[origmix][origkey]")
groups["VOICE"].append("[origmix]")
k = 1
for f, a, b, tgt, fi, fo, g, filt in BEDS:
    p = f"{S}/{f}"; gain = tgt - lufs(p); d = b - a
    inputs += ["-stream_loop","-1","-i",p]
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo" + (f",{filt}" if filt else "") +
              f",atrim=0:{d},asetpts=N/SR/TB,volume={gain:.1f}dB,afade=t=in:d={fi},afade=t=out:st={max(0,d-fo):.3f}:d={fo},"
              f"adelay={int(a*1000)}:all=1[x{k}]")
    groups[g].append(f"[x{k}]"); k += 1
for t, f, db, pan, filt, al, g in SPOTS:
    p = f"{S}/{f}"; gain = -1 - peak(p) + db; st = max(0.0, t - (onset(p) if al else 0.0))
    lg, rg = min(1.0, 1-pan), min(1.0, 1+pan)
    inputs += ["-i", p]
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,volume={gain:.1f}dB" + (f",{filt}" if filt else "") +
              f",aformat=channel_layouts=mono,pan=stereo|c0={lg:.2f}*c0|c1={rg:.2f}*c0,adelay={int(st*1000)}:all=1[x{k}]")
    groups[g].append(f"[x{k}]"); k += 1
def bus(name, labs):
    fl.append("".join(labs) + f"amix=inputs={len(labs)}:normalize=0:duration=longest[{name}]")
bus("voice", groups["VOICE"]); fl.append("[voice]asplit=2[voiceout][voicekey0]")
fl.append("[voicekey0][origkey]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo[key]")
bus("amb0", groups["AMB"]); bus("fx", groups["FX"]); bus("mus", groups["MUS"])
fl.append("[amb0][key]sidechaincompress=threshold=0.015:ratio=8:attack=15:release=450:makeup=1[amb]")
fl.append(f"[voiceout][amb][fx][mus]amix=inputs=4:normalize=0:duration=longest,atrim=0:{TOTAL},aformat=sample_fmts=fltp:channel_layouts=stereo[mix]")
open("mix_v3_filter.txt","w").write(";\n".join(fl))
r = run(["ffmpeg","-v","error","-y"] + inputs + ["-filter_complex",";".join(fl),"-map","[mix]","-c:a","pcm_f32le","-ar","48000",TMP])
if r.returncode: print(r.stderr[-3000:]); raise SystemExit(1)
I = lufs(TMP); g = -17.0 - I; print(f"pre-master {I:.1f} LUFS -> gain {g:+.1f} dB")
r = run(["ffmpeg","-v","error","-y","-i",CUT,"-i",TMP,"-filter_complex",
         f"[1:a]volume={g:.2f}dB,alimiter=limit=0.84:attack=2:release=60[a]","-map","0:v","-map","[a]",
         "-c:v","copy","-c:a","aac","-b:a","256k","-ar","48000",OUT])
if r.returncode: print(r.stderr[-2000:]); raise SystemExit(1)
print("ok", OUT, f"final {lufs(OUT):.1f} LUFS")
