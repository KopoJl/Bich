# Рисует часы 03:06 и 03:07 поверх циферблата SH140 (камера статична).
import sys, math
from PIL import Image, ImageDraw, ImageFilter
src, out_dir = sys.argv[1], sys.argv[2]
CX, CY, R_ERASE = 676, 214, 19
im = Image.open(src).convert("RGB")
box = (CX-32, CY-32, CX+32, CY+32)
crop = im.crop(box)
px = crop.load()
# цвет циферблата: медиана светлых пикселей в кольце r 8..18
vals = []
for y in range(64):
    for x in range(64):
        r = math.hypot(x-32, y-32)
        if 8 < r < 18:
            p = px[x, y]
            if sum(p) > 330: vals.append(p)
vals.sort(key=sum); face = vals[len(vals)//2]
# стираем всё тёмное внутри r < R_ERASE (старые стрелки)
for y in range(64):
    for x in range(64):
        if math.hypot(x-32, y-32) < R_ERASE and sum(px[x, y]) < sum(face) - 60:
            px[x, y] = face
crop = crop.filter(ImageFilter.SMOOTH) if False else crop
def draw(h, m, name):
    S = 8
    big = crop.resize((64*S, 64*S), Image.LANCZOS)
    d = ImageDraw.Draw(big)
    c = (32*S, 32*S); ink = (38, 36, 40)
    ma = math.radians(m*6 - 90); ha = math.radians((h % 12)*30 + m*0.5 - 90)
    d.line([c, (c[0]+17*S*math.cos(ma), c[1]+17*S*math.sin(ma))], fill=ink, width=int(1.5*S))
    d.line([c, (c[0]+11*S*math.cos(ha), c[1]+11*S*math.sin(ha))], fill=ink, width=int(2.3*S))
    d.ellipse([c[0]-1.6*S, c[1]-1.6*S, c[0]+1.6*S, c[1]+1.6*S], fill=ink)
    small = big.resize((64, 64), Image.LANCZOS)
    # круглая маска, чтобы не трогать обои и обод
    mask = Image.new("L", (64, 64), 0)
    ImageDraw.Draw(mask).ellipse([32-R_ERASE, 32-R_ERASE, 32+R_ERASE, 32+R_ERASE], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(0.8))
    rgba = small.convert("RGBA"); rgba.putalpha(mask)
    rgba.save(f"{out_dir}/{name}.png")
draw(3, 6, "clock_0306"); draw(3, 7, "clock_0307")
print("face", face, "box", box)
