# «03:06» — вертикальная версия 9:16 для TikTok / Instagram Reels / YouTube Shorts.
# Холст 1080×1920: сверху полоса 300 с названием (ниже вкладок приложения), картинка 3:4 (1080×1440, y 300–1740),
# снизу 180 — зона интерфейса TikTok/Reels. Субтитры — на нижней трети картинки (y≈1390), вне нижних ~450 px.
# Кадрирование 3:4 внутри 16:9 выбрано по каждому шоту (FRAME: центр кадра в долях ширины, начало → конец).
# Источник — отгрейденный монтаж 07_montage/edit_v2_video.mp4 и его таймлайн; финишинг (свечение, зерно,
# виньетка) делается заново уже в вертикальном размере; звук — мастер v5, приведённый к −14 LUFS.
import json, os, subprocess, re
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
SRC = "../07_montage/edit_v2_video.mp4"; TL = json.load(open("../07_montage/work_v2/timeline.json"))
MIX = "/tmp/claude-0/-home-user-Bich/939377ca-f5da-57b2-867a-fc6105a9df4e/scratchpad/mix_v5.wav"
W = "work"; os.makedirs(W, exist_ok=True); OUT = "0306_vertical_9x16.mp4"
FONT = "/usr/share/fonts/opentype/inter/"
FRAME = {   # центр кадра 3:4 в долях ширины 16:9: (начало, конец)
 "SH010": (0.33, 0.42), "SH020": (0.45, 0.45), "SH030": (0.36, 0.60), "SH040a": (0.50, 0.50), "EYE": (0.50, 0.50),
 "SH040b": (0.50, 0.50), "SH050": (0.34, 0.40), "SH060": (0.45, 0.45), "SH070": (0.42, 0.42), "SH080": (0.42, 0.52),
 "BLINK1": (0.5, 0.5), "SH090": (0.42, 0.42), "SH100a": (0.50, 0.50), "SLIP1": (0.45, 0.45), "SLIP2": (0.47, 0.47),
 "SH100b": (0.50, 0.52), "SH100c": (0.55, 0.55), "BLACK2": (0.5, 0.5), "SH110a": (0.42, 0.42), "SH110b": (0.50, 0.50),
 "BLINK2": (0.5, 0.5), "SH115": (0.42, 0.50), "SH120": (0.45, 0.45), "SH125": (0.38, 0.40), "SH130": (0.50, 0.50),
 "SH135": (0.45, 0.48), "BLACK3": (0.5, 0.5),
}
ENC = ["-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-r","24","-an"]
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2000:]); raise SystemExit(1)
    return r

# ---- вертикальные титры (картинка 1080×1440)
def spaced(d, cx, y, text, f, fill, track):
    w = sum(d.textlength(ch, font=f) for ch in text) + track*(len(text)-1); x = cx - w/2
    for ch in text: d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track
INK, DIM = (226,222,212), (150,148,142)
im = Image.new("RGB", (1080,1440)); d = ImageDraw.Draw(im)
spaced(d, 540, 560, "03:06", ImageFont.truetype(FONT+"Inter-ExtraLight.otf", 170), INK, 24)
spaced(d, 540, 800, "LONDON · NOVEMBER 1977", ImageFont.truetype(FONT+"Inter-Regular.otf", 30), DIM, 10)
im.save(f"{W}/title_v.png")
im = Image.new("RGB", (1080,1440)); d = ImageDraw.Draw(im)
spaced(d, 540, 560, "03:06", ImageFont.truetype(FONT+"Inter-ExtraLight.otf", 110), INK, 18)
author = os.environ.get("AUTHOR","").strip(); y = 760
if author:
    spaced(d, 540, y, "WRITTEN AND DIRECTED BY", ImageFont.truetype(FONT+"Inter-Regular.otf", 24), DIM, 8); y += 48
    spaced(d, 540, y, author.upper(), ImageFont.truetype(FONT+"Inter-Light.otf", 40), INK, 6); y += 110
spaced(d, 540, y, "MADE WITH", ImageFont.truetype(FONT+"Inter-Regular.otf", 22), DIM, 8)
spaced(d, 540, y+44, "gpt-image-2 · Seedream 5.0", ImageFont.truetype(FONT+"Inter-Light.otf", 30), DIM, 2)
spaced(d, 540, y+88, "Seedance 2.5 · Higgsfield", ImageFont.truetype(FONT+"Inter-Light.otf", 30), DIM, 2)
im.save(f"{W}/credits_v.png")

# ---- сегменты по таймлайну (наплыв SH135→SH140 — один сегмент)
clips = TL["clips"]; segs = []
for c in clips:
    if c["id"] == "SH140": continue
    t0 = c["t0"]; dur = c["out"] - c["in"]
    if c["id"] == "SH135":
        s140 = next(x for x in clips if x["id"] == "SH140"); dur = s140["t0"] + (s140["out"] - s140["in"]) - t0
    segs.append((c["id"], t0, dur))
files = []
for i, (cid, t0, dur) in enumerate(segs):
    n = int(round(dur*24)); o = f"{W}/{i:02d}_{cid}.mp4"
    if cid in ("TITLE", "CREDITS"):
        png = f"{W}/title_v.png" if cid == "TITLE" else f"{W}/credits_v.png"
        fi, fo = (0.8, 0.7) if cid == "TITLE" else (1.0, 1.0)
        run(["ffmpeg","-v","error","-y","-loop","1","-framerate","24","-i",png,"-frames:v",str(n),"-vf",
             f"fade=t=in:st=0:d={fi},fade=t=out:st={dur-fo:.3f}:d={fo}"] + ENC + [o])
    else:
        x0, x1 = FRAME.get(cid, (0.5, 0.5))
        X = f"(iw*({x0}+({x1}-{x0})*(0.5-0.5*cos(PI*t/{dur:.3f})))-270)"
        run(["ffmpeg","-v","error","-y","-ss",f"{t0:.4f}","-i",SRC,"-frames:v",str(n),"-vf",
             f"crop=540:720:x='max(0,min(iw-540,{X}))':y=0,scale=1080:1440:flags=lanczos,unsharp=5:5:0.4:5:5:0,setsar=1"] + ENC + [o])
    files.append(o)
with open(f"{W}/list.txt","w") as f:
    for p in files: f.write(f"file '{os.path.basename(p)}'\n")
run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{W}/list.txt","-c","copy",f"{W}/picture.mp4"])

# ---- надписи: название сверху (кроме титров), субтитры снизу
CL = {c["id"]: c for c in clips}
def T(cid, local=None): c = CL[cid]; return c["t0"] if local is None else c["t0"] + (local - c["in"])
SUBS = [  # (начало, конец, пометка, реплика)
 (T("SH010",0.25), T("SH010",2.35), "", "Three-oh-six. The house is quiet."),
 (T("SH030",1.70), T("SH030",2.80), "", "Pipes."),
 (T("SH110a",1.60), T("SH110a",2.75), "ON TAPE", "Three-oh-six."),
 (T("SH115")-0.12, T("SH115")+2.2, "ON TAPE", "Three-oh-six. The house is quiet."),
 (T("SH125",1.20), T("SH125",4.80), "ON TAPE · SLOWING TO A WHISPER", "Three-oh-six…"),
]
def txt(name, s): p = f"{W}/{name}.txt"; open(p,"w").write(s); return p
draw = []
tt, tc = T("TITLE"), T("CREDITS")
draw.append(f"drawtext=fontfile={FONT}Inter-ExtraLight.otf:textfile={txt('top','03:06')}:fontsize=58:fontcolor=0xE2DED4@0.85:"
            f"x=(w-text_w)/2:y=238-text_h/2:enable='not(between(t,{tt:.3f},{tt+3.3:.3f}))*lt(t,{tc:.3f})'")
for i, (a, b, tag, line) in enumerate(SUBS):
    if tag:
        draw.append(f"drawtext=fontfile={FONT}Inter-Medium.otf:textfile={txt(f'tag{i}',tag)}:fontsize=28:fontcolor=0xC8C6BE:borderw=2:bordercolor=black@0.7:"
                    f"x=(w-text_w)/2:y={1318 if len(line) > 20 else 1346}:enable='between(t,{a:.3f},{b:.3f})'")
    parts = [x.strip() for x in re.split(r"(?<=\.) ", line)] if len(line) > 20 else [line]   # длинное — в две строки
    y0 = 1388 if len(parts) == 1 else 1360
    for j, part in enumerate(parts):
        draw.append(f"drawtext=fontfile={FONT}Inter-Medium.otf:textfile={txt(f'sub{i}_{j}',part)}:fontsize=52:fontcolor=white:"
                    f"borderw=3:bordercolor=black@0.85:shadowx=0:shadowy=2:shadowcolor=black@0.6:x=(w-text_w)/2:y={y0+j*62}:enable='between(t,{a:.3f},{b:.3f})'")
FC = ("[0:v]format=gbrp,split[a][b];[b]curves=all='0/0 0.66/0 1/1',gblur=sigma=22[g];"
      "[a][g]blend=all_mode=screen:all_opacity=0.42,format=yuv420p,vignette=angle=PI/8:mode=forward,"
      "noise=c0s=7:c0f=t+u:c1s=2:c1f=t+u:c2s=2:c2f=t+u,pad=1080:1920:0:300:black," + ",".join(draw) + "[v];"
      "[1:a]volume={g}dB,alimiter=limit=0.84:attack=2:release=60,apad[a]")
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg","-hide_banner","-i",MIX,"-af","ebur128","-f","null","-"],capture_output=True,text=True).stderr)[-1])
g = -14.6 - I   # лимитер добавляет ≈ +1 LU → итог ≈ −14 LUFS
run(["ffmpeg","-v","error","-y","-i",f"{W}/picture.mp4","-i",MIX,"-filter_complex",FC.format(g=f"{g:.2f}"),"-map","[v]","-map","[a]",
     "-c:v","libx264","-preset","slow","-crf","20","-maxrate","10M","-bufsize","20M","-tune","grain","-pix_fmt","yuv420p","-r","24",
     "-c:a","aac","-b:a","256k","-ar","48000","-movflags","+faststart","-t",f"{TL['total']:.3f}",OUT])
print("ok", OUT)
