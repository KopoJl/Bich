# Титры «03:06»: заглавный и финальный. Inter (гротеск в духе титров 70-х), off-white на чёрном.
from PIL import Image, ImageDraw, ImageFont
W, H = 1920, 1080; INK = (226, 222, 212); DIM = (150, 148, 142)
F = "/usr/share/fonts/opentype/inter/"
def font(n, s): return ImageFont.truetype(F + n, s)
def spaced(d, xy, text, f, fill, track, anchor_center=True):
    w = sum(d.textlength(ch, font=f) for ch in text) + track * (len(text) - 1)
    x = xy[0] - w / 2 if anchor_center else xy[0]
    for ch in text:
        d.text((x, xy[1]), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track
# заглавный
im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
spaced(d, (W/2, 420), "03:06", font("Inter-ExtraLight.otf", 190), INK, 36)
spaced(d, (W/2, 690), "LONDON  ·  NOVEMBER 1977", font("Inter-Regular.otf", 26), DIM, 12)
im.save("title.png")
# финальные
import os
AUTHOR = os.environ.get("AUTHOR", "").strip()      # имя автора: AUTHOR="..." python3 make_titles.py
CREDITS = [("03:06", "Inter-ExtraLight.otf", 96, INK, 22, 0), ("", None, 0, None, 0, 50)]
if AUTHOR:
    CREDITS += [("WRITTEN AND DIRECTED BY", "Inter-Regular.otf", 20, DIM, 10, 0),
                (AUTHOR.upper(), "Inter-Light.otf", 40, INK, 8, 0), ("", None, 0, None, 0, 50)]
CREDITS += [("MADE WITH", "Inter-Regular.otf", 18, DIM, 10, 0),
            ("gpt-image-2  ·  Seedream 5.0  ·  Seedance 2.5  ·  Higgsfield", "Inter-Light.otf", 24, DIM, 3, 0)]
im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
heights = [(s * 1.6 if t else g) for t, _, s, _, _, g in CREDITS]; y = (H - sum(heights)) / 2
for (t, fn, s, c, tr, g), h in zip(CREDITS, heights):
    if t: spaced(d, (W/2, y), t, font(fn, s), c, tr)
    y += h
im.save("credits.png"); print("ok")
