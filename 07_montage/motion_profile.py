# Покадровое движение дубля: средняя разница соседних кадров (0..255). Печатает профиль по 0,25 с.
import sys, subprocess, re
f = sys.argv[1]
out = subprocess.run(["ffmpeg","-v","error","-i",f,"-vf","scale=320:-1,format=gray,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-","-an","-f","null","-"],capture_output=True,text=True).stdout
v = [float(x) for x in re.findall(r"YAVG=([\d.]+)", out)]
step = 6; rows = []
for i in range(0, len(v), step):
    seg = v[i:i+step]; rows.append(f"{i/24:.2f}:{sum(seg)/len(seg):.1f}")
print(f.split('/')[-1], " ".join(rows))
