# Субтитры EN/RU по таймлайну монтажа (work_v2/timeline.json).
import json
TL = json.load(open("../07_montage/work_v2/timeline.json")); CL = {c["id"]: c for c in TL["clips"]}
def T(cid, local=None):
    c = CL[cid]; return c["t0"] if local is None else c["t0"] + (local - c["in"])
LINES = [  # (начало, конец, EN, RU)
 (T("SH010",0.25), T("SH010",2.35), "Three-oh-six. The house is quiet.", "Три ноль шесть. В доме тихо."),
 (T("SH030",1.70), T("SH030",2.80), "Pipes.", "Трубы."),
 (T("SH110a",1.60), T("SH110a",2.75), "[ON TAPE] Three-oh-six.", "[С ПЛЁНКИ] Три ноль шесть."),
 (T("SH115",0.0)-0.12, T("SH115",0.0)+2.2, "[ON TAPE] Three-oh-six. The house is quiet.", "[С ПЛЁНКИ] Три ноль шесть. В доме тихо."),
 (T("SH125",1.20), T("SH125",4.80), "[ON TAPE, SLOWING TO A WHISPER] Three-oh-six…", "[С ПЛЁНКИ, ЗАМЕДЛЯЯСЬ В ШЁПОТ] Три ноль шесть…"),
]
def ts(t):
    t = max(0, t); h = int(t//3600); m = int(t%3600//60); s = t%60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s-int(s))*1000)):03d}"
for lang, idx in (("en", 2), ("ru", 3)):
    with open(f"../07_montage/0306_{lang}.srt", "w", encoding="utf-8") as f:
        for i, l in enumerate(LINES, 1): f.write(f"{i}\n{ts(l[0])} --> {ts(l[1])}\n{l[idx]}\n\n")
print("ok")
