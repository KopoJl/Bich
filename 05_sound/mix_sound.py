# Звуковая сборка «03:06»: оригинальный звук монтажа + эффекты Higgsfield (Mirelo) по таймкодам.
# Запуск: python3 -I mix_sound.py  (из папки 05_sound). Выход: ../07_montage/0306_cut_v2.mp4
import subprocess, struct, os
SFX = "sfx"; CUT = "../07_montage/0306_roughcut_v1.mp4"; OUT = "../07_montage/0306_cut_v2.mp4"
TOTAL = 87.30

def onset(path, thr_db=30):
    raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout
    s = struct.unpack("<%dh" % (len(raw)//2), raw)
    peak = max(1, max(abs(x) for x in s)); th = peak * 10**(-thr_db/20)
    for i, x in enumerate(s):
        if abs(x) >= th: return max(0.0, i/8000 - 0.01)
    return 0.0

# (время на монтаже, файл, громкость dB, панорама -1..1, [фильтр], выровнять_по_атаке)
SPOTS = [
 # SH010
 (5.50,"stop_clack.mp3",-6,0,"",True),
 # SH020
 (7.90,"teacup_clink.mp3",-12,0,"",True),
 (8.00,"bus_night.mp3",-12,0.5,"lowpass=f=2500",False),
 (11.00,"creak_upstairs.mp3",-8,0,"lowpass=f=3000",True),
 # SH030 — скрип ступеньки за дверью (дверь слева)
 (13.40,"creak_stair.mp3",-10,-0.4,"lowpass=f=2500",True),
 # SH040 — реле, щелчок 1/2
 (19.60,"relay_click.mp3",-3,0,"",True),
 # SH050 — из шкафа справа: капли и мокрое дыхание; чашка; перемотка
 (22.75,"cupboard_drips.mp3",-14,0.7,"",False),
 (23.30,"teacup_clink.mp3",-18,0,"",True),
 (27.70,"tape_rewind.mp3",-10,0,"",False),
 # SH060 — PLAY на первом кадре
 (28.75,"play_clack.mp3",-4,0,"",True),
 # SH070 — проигрыватель слева
 (35.55,"needle_drop.mp3",-8,-0.6,"",True),
 (35.70,"music_box.mp3",-14,-0.6,"",False),
 (37.40,"torch_grab.mp3",-10,0,"",True),
 (39.60,"chair_creak.mp3",-10,0,"",True),
 # SH080 — лампа гаснет, капли из шкафа (мост), щелчки фонарика в тишине
 (41.30,"lamp_click.mp3",-6,-0.3,"",True),
 (41.90,"cupboard_drips.mp3",-14,0,"afade=t=out:st=0.6:d=0.25",False),
 (44.95,"torch_click.mp3",0,-0.3,"",True),
 (45.40,"torch_click.mp3",0,-0.3,"",True),
 (46.00,"torch_click.mp3",0,-0.3,"",True),
 (46.25,"torch_rattle.mp3",-6,0,"",True),
 # SH090 — стингер на первом кадре
 (46.54,"violin_stab.mp3",-9,0,"",True),
 (46.60,"coat_drips.mp3",-14,0,"",False),
 # SH100 — бег, тапок, стук в стенах, дверца, фонарик гаснет
 (48.17,"run_hall.mp3",-6,0,"afade=t=out:st=5.6:d=0.3",False),
 (49.50,"wall_knocks.mp3",-16,-0.7,"",False),
 (50.90,"wall_knocks.mp3",-17,0.7,"",False),
 (50.30,"slipper_drop.mp3",-6,0,"",True),
 (52.20,"small_door.mp3",-6,0.3,"",True),
 (53.00,"torch_rattle.mp3",-6,0,"",True),
 (53.35,"torch_rattle.mp3",-6,0,"",True),
 # SH110a — рубильник, голос с плёнки СЗАДИ, разворот
 (55.00,"fuse_clunk.mp3",-4,0.4,"",True),
 (55.45,"fuse_clunk.mp3",-5,0.4,"",True),
 (55.85,"fuse_clunk.mp3",-4,0.4,"",True),
 (56.23,"ruth_voice_306.wav",-4,0,"highpass=f=300,lowpass=f=3200,aecho=0.8:0.7:60:0.3,lowpass=f=1800",False),
 (58.30,"whoosh.mp3",-4,0,"",True),
 # SH110b — удар низких струнных на приземлении, голос спереди
 (58.63,"low_strings.mp3",-7,0,"",True),
 (58.70,"coat_drips.mp3",-14,0,"",False),
 # мигание — исчез
 (60.30,"torch_rattle.mp3",-6,0,"",True),
 # SH115 — неровные шаги, голос из комнаты в нормальном темпе
 (60.43,"steps_sock.mp3",-8,0,"",False),
 (60.60,"ruth_voice_full.wav",-8,0,"highpass=f=300,lowpass=f=3200,aecho=0.8:0.6:40:0.25",False),
 # SH120 — голос начинает замедляться, шаги Рут приближаются
 (63.00,"ruth_voice_full.wav",-6,0,"highpass=f=250,lowpass=f=3000,asetrate=48000*0.8,aresample=48000",False),
 (64.40,"steps_sock.mp3",-14,-0.3,"",False),
 (62.70,"coat_drips.mp3",-15,0.2,"",False),
 # SH125 — голос опускается в шёпот (её собственный), фонарик падает
 (66.60,"ruth_voice_full.wav",-4,0,"highpass=f=200,lowpass=f=2600,asetrate=48000*0.6,aresample=48000,aecho=0.8:0.5:80:0.3",False),
 (66.47,"scared_breath.mp3",-12,0,"",False),
 (69.95,"torch_drop.mp3",-6,0,"",True),
 # SH130 — кассета, лента, обрыв, магнитофон падает
 (72.30,"eject.mp3",-6,0,"",True),
 (73.60,"tape_pull.mp3",-8,0,"",False),
 (75.72,"tape_snap.mp3",-2,0,"",True),
 (76.37,"recorder_drop.mp3",-6,0,"",True),
 # SH135 — выдох, далёкий автобус
 (77.60,"scared_breath.mp3",-14,0,"",False),
 (79.20,"bus_night.mp3",-22,0.6,"lowpass=f=1500",False),
 # SH140 — утро, даблдекер справа налево, дыхание во сне, реле 2/2
 (80.60,"bus_morning.mp3",-10,0,"",False),
 (80.50,"sleep_breath.mp3",-18,-0.2,"",False),
 (86.07,"relay_click.mp3",-2,0,"",True),
]
# подложки: (файл, начало, конец, dB, fade_in, fade_out)
BEDS = [
 ("rain_bed.mp3", 0.00, 42.75, -14, 0.5, 0.2),
 ("drone.mp3",   22.75, 42.75, -14, 3.0, 0.1),
 ("motor_hiss.mp3", 0.00, 6.00, -22, 0.2, 0.3),
 ("motor_hiss.mp3", 28.75, 34.75, -24, 0.1, 0.5),
 ("drone.mp3",   46.54, 75.72, -10, 0.1, 0.02),
 ("motor_hiss.mp3", 62.63, 75.72, -22, 0.5, 0.02),
 ("rain_bed.mp3", 77.47, 81.50, -16, 1.5, 2.0),
 ("morning_amb.mp3", 79.50, 86.30, -12, 2.0, 0.02),
]
# оригинальный звук монтажа: тише и в ноль там, где мёртвая тишина
ORIG_DB = -3
MUTE = [(42.75, 46.38), (54.33, 54.63), (75.72, 77.47), (86.30, TOTAL)]

inputs = ["-i", CUT]; fl = []; labels = []
mute_expr = "+".join(f"between(t,{a},{b})" for a, b in MUTE)
fl.append(f"[0:a]aresample=48000,volume={ORIG_DB}dB,volume=0:enable='{mute_expr}'[orig]"); labels.append("[orig]")
k = 1
for f, a, b, db, fi, fo in BEDS:
    inputs += ["-stream_loop", "-1", "-i", f"{SFX}/{f}"]; d = b - a
    fl.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{d},asetpts=N/SR/TB,volume={db}dB,"
              f"afade=t=in:d={fi},afade=t=out:st={d-fo}:d={fo},adelay={int(a*1000)}:all=1[b{k}]"); labels.append(f"[b{k}]"); k += 1
for t, f, db, pan, extra, align in SPOTS:
    p = f"{SFX}/{f}"; off = onset(p) if align else 0.0
    start = max(0.0, t - off)
    lg = min(1.0, 1 - pan); rg = min(1.0, 1 + pan)
    inputs += ["-i", p]
    chain = f"[{k}:a]aresample=48000,aformat=channel_layouts=mono" + (f",{extra}" if extra else "") + \
            f",aformat=channel_layouts=mono,pan=stereo|c0={lg:.2f}*c0|c1={rg:.2f}*c0,volume={db}dB,adelay={int(start*1000)}:all=1[s{k}]"
    fl.append(chain); labels.append(f"[s{k}]"); k += 1
fl.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,loudnorm=I=-18:LRA=18:TP=-1.5,alimiter=limit=0.84,atrim=0:{TOTAL}[aout]")
cmd = ["ffmpeg","-v","error","-y"] + inputs + ["-filter_complex", ";".join(fl), "-map","0:v","-map","[aout]",
       "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000", OUT]
open("mix_filter.txt","w").write(";\n".join(fl))
subprocess.run(cmd, check=True); print("ok", OUT)
