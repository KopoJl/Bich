# Сборка видео по монтажному листу edl.py. Запуск из 07_montage: python3 -I build_edit.py
import subprocess, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edl import CLIPS, DISSOLVE, FADE_OUT, FADE_IN, WHIP_BLUR_FRAMES, GRADE, timeline
W = "work_v2"; os.makedirs(W, exist_ok=True)
ENC = ["-c:v","libx264","-preset","medium","-crf","17","-pix_fmt","yuv420p","-r","24","-an"]
BASE = "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=24"   # без растяжения 1256→1280

def move_filter(mv, dur):
    if not mv: return BASE
    n = max(1, int(round(dur * 24)))
    up = "scale=2560:1440:force_original_aspect_ratio=increase:flags=lanczos,crop=2560:1440,setsar=1,fps=24"
    if mv[0] == "push":
        z0, z1 = mv[1], mv[2]
        # плавный наезд/дрейф к центру (ease-in-out), d=1 — один выходной кадр на входной
        z = f"{z0}+({z1}-{z0})*(0.5-0.5*cos(PI*on/{n}))"
        return f"{up},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1280x720:fps=24,setsar=1"
    if mv[0] == "pan":
        z, x0, x1 = mv[1], mv[2], mv[3]
        x = f"(iw-iw/zoom)*({x0}+({x1}-{x0})*(0.5-0.5*cos(PI*on/{n})))"
        return f"{up},zoompan=z='{z}':x='{x}':y='ih/2-(ih/zoom/2)':d=1:s=1280x720:fps=24,setsar=1"

def render(i, cid, f, a, b, mv):
    o = f"{W}/{i:02d}_{cid}.mp4"; d = b - a
    if f is None:
        cmd = ["ffmpeg","-v","error","-y","-f","lavfi","-i",f"color=black:s=1280x720:r=24","-t",f"{d}"] + ENC + [o]
    else:
        vf = move_filter(mv, d)
        if cid in GRADE: vf += "," + GRADE[cid]
        if cid in FADE_IN: vf += f",fade=t=in:st=0:d={FADE_IN[cid]}"
        if cid in FADE_OUT: vf += f",fade=t=out:st={d-FADE_OUT[cid]:.3f}:d={FADE_OUT[cid]}"
        if cid in WHIP_BLUR_FRAMES:
            k = WHIP_BLUR_FRAMES[cid]
            vf += f",gblur=sigma=40:sigmaV=0.5:enable='lt(n,{k})'"
        if f.endswith(".png"):
            cmd = ["ffmpeg","-v","error","-y","-loop","1","-framerate","24","-i",f,"-t",f"{d}","-vf",vf] + ENC + [o]
        elif cid == "SH140":   # часы 03:06 → 03:07 на 5,6 с времени дубля — ДО грейдинга
            sw = 5.6 - a
            fc = (f"[0:v]scale=1280:720,setsar=1[s];[s][1]overlay=644:182:enable='lt(t,{sw})'[c1];"
                  f"[c1][2]overlay=644:182:enable='gte(t,{sw})',{vf}[v]")
            cmd = ["ffmpeg","-v","error","-y","-ss",f"{a}","-to",f"{b}","-i",f,"-i","work/clock_0306.png","-i","work/clock_0307.png",
                   "-filter_complex",fc,"-map","[v]"] + ENC + [o]
        else:
            cmd = ["ffmpeg","-v","error","-y","-ss",f"{a}","-to",f"{b}","-i",f,"-vf",vf] + ENC + [o]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); raise SystemExit(cid)
    return o

files = []
for i, (cid, f, a, b, mv, note) in enumerate(CLIPS):
    files.append((cid, render(i, cid, f, a, b, mv)))

# наплыв SH135 → SH140
c1, c2, dd = DISSOLVE
i1 = [c for c, _ in files].index(c1); i2 = i1 + 1
d1 = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",files[i1][1]],capture_output=True,text=True).stdout)
mixf = f"{W}/xfade_{c1}_{c2}.mp4"
subprocess.run(["ffmpeg","-v","error","-y","-i",files[i1][1],"-i",files[i2][1],"-filter_complex",
  f"[0][1]xfade=transition=fade:duration={dd}:offset={d1-dd:.3f}"] + ENC + [mixf], check=True)
files = files[:i1] + [("X", mixf)] + files[i2+1:]

with open(f"{W}/list.txt","w") as fh:
    for _, p in files: fh.write(f"file '{os.path.basename(p)}'\n")
subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{W}/list.txt","-c","copy","edit_v2_video.mp4"], check=True)
print("video ok", timeline()[1])

# --- реальные позиции клипов (после округления до кадров) для сведения звука
import json
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-select_streams","v","-count_frames","-show_entries","stream=nb_read_frames","-of","csv=p=0",p],capture_output=True,text=True).stdout)/24
real, t = [], 0.0
src = {c: (a, b) for c, f, a, b, m, n in CLIPS}
for cid, p in files:
    d = dur(p)
    if cid == "X":
        d135 = dur(f"{W}/" + [x for x in os.listdir(W) if x.endswith(f"_{DISSOLVE[0]}.mp4")][0])
        a1 = src[DISSOLVE[0]][0]; a2 = src[DISSOLVE[1]][0]
        real.append({"id": DISSOLVE[0], "in": a1, "out": a1 + d135, "t0": t})
        real.append({"id": DISSOLVE[1], "in": a2, "out": a2 + (d - (d135 - DISSOLVE[2])), "t0": t + d135 - DISSOLVE[2]})
    else:
        a = src[cid][0]; real.append({"id": cid, "in": a, "out": a + d, "t0": t})
    t += d
json.dump({"clips": real, "total": t}, open(f"{W}/timeline.json", "w"), indent=1)
print("timeline.json total", round(t, 3))
