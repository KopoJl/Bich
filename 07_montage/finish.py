# Финишинг: 1080p (lanczos + мягкая резкость), свечение ярких источников (лампа, фонарик, окно),
# единое плёночное зерно поверх разных генераций, лёгкая виньетка. Вход: edit_v2_video.mp4.
import subprocess, sys
SRC = "edit_v2_video.mp4"; OUT = sys.argv[1] if len(sys.argv) > 1 else "edit_v3_1080.mp4"
EXTRA = sys.argv[2:]   # например -ss 40 -t 6 для пробы
FC = ("[0:v]scale=1920:1080:flags=lanczos,unsharp=5:5:0.35:5:5:0,format=gbrp,split[a][b];"
      "[b]curves=all='0/0 0.66/0 1/1',gblur=sigma=26[glow];"
      "[a][glow]blend=all_mode=screen:all_opacity=0.42,format=yuv420p,"
      "vignette=angle=PI/8:mode=forward,"
      "noise=c0s=7:c0f=t+u:c1s=2:c1f=t+u:c2s=2:c2f=t+u[v]")
cmd = ["ffmpeg","-v","error","-y"] + EXTRA + ["-i",SRC,"-filter_complex",FC,"-map","[v]",
       "-c:v","libx264","-preset","slow","-crf","16","-tune","grain","-pix_fmt","yuv420p","-r","24","-an",OUT]
subprocess.run(cmd, check=True); print("ok", OUT)
