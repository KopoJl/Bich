# Обложки «03:06»: вертикальная 1080×1920 (TikTok / Reels / Shorts) и 1280×720 (превью YouTube / Facebook).
# Кадр — лицо Рут в момент узнавания (SH125), из отгрейденного монтажа; крупное название.
import json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TL = {c["id"]: c for c in json.load(open("../07_montage/work_v2/timeline.json"))["clips"]}
c = TL["SH125"]; t = c["t0"] + (3.0 - c["in"])
subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{t:.3f}","-i","../07_montage/edit_v2_video.mp4","-frames:v","1","work/cover_src.png"], check=True)
F = "/usr/share/fonts/opentype/inter/"; INK = (236,232,222); DIM = (170,168,160)
src = Image.open("work/cover_src.png").convert("RGB")
src = ImageEnhance.Brightness(src).enhance(1.18); src = ImageEnhance.Contrast(src).enhance(1.08)
def spaced(d, cx, y, text, f, fill, track):
    w = sum(d.textlength(ch, font=f) for ch in text) + track*(len(text)-1); x = cx - w/2
    for ch in text: d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track
def shade(im, top, bottom):   # затемнение сверху/снизу, чтобы текст читался
    g = Image.new("L", (1, 256))
    for y in range(256): g.putpixel((0, y), int(255*max(top*(1-y/90) if y < 90 else 0, bottom*((y-166)/90) if y > 166 else 0)))
    m = g.resize(im.size); im.paste(Image.new("RGB", im.size), (0,0), m); return im
# вертикальная: кадр 3:4 вокруг лица (центр 0.38) → 1080×1440, на холсте 1080×1920
w, h = src.size; cw = int(h*3/4); x = max(0, min(w-cw, int(w*0.38 - cw/2)))
pic = src.crop((x, 0, x+cw, h)).resize((1080, 1440), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
V = Image.new("RGB", (1080, 1920)); V.paste(pic, (0, 300)); V = shade(V, 0.0, 0.95); d = ImageDraw.Draw(V)
spaced(d, 540, 1150, "03:06", ImageFont.truetype(F+"Inter-ExtraLight.otf", 190), INK, 26)
spaced(d, 540, 1385, "SHE RECORDED AN EMPTY ROOM.", ImageFont.truetype(F+"Inter-Regular.otf", 30), DIM, 6)
spaced(d, 540, 1431, "SOMETHING ANSWERED.", ImageFont.truetype(F+"Inter-Regular.otf", 30), DIM, 6)
V.save("cover_vertical_1080x1920.jpg", quality=92)
# горизонтальная превью: кадр целиком, название справа
H = src.resize((1280, 720), Image.LANCZOS); H = shade(H, 0.0, 0.0); d = ImageDraw.Draw(H)
ov = Image.new("L", (1280, 720), 0); od = ImageDraw.Draw(ov)
for xx in range(640, 1280): od.line([(xx, 0), (xx, 720)], fill=int(200*(xx-640)/640))
H.paste(Image.new("RGB", H.size), (0,0), ov); d = ImageDraw.Draw(H)
spaced(d, 1000, 270, "03:06", ImageFont.truetype(F+"Inter-ExtraLight.otf", 150), INK, 18)
spaced(d, 1000, 470, "SHE RECORDED AN EMPTY ROOM.", ImageFont.truetype(F+"Inter-Regular.otf", 20), DIM, 4)
spaced(d, 1000, 502, "SOMETHING ANSWERED.", ImageFont.truetype(F+"Inter-Regular.otf", 20), DIM, 4)
H.save("cover_youtube_1280x720.jpg", quality=92); print("ok")
