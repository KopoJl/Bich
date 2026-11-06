#!/usr/bin/env bash
# Черновой монтаж «03:06» по точкам склеек из log.md. Запуск из папки 07_montage.
set -euo pipefail
T=../06_takes; W=work; mkdir -p $W
ENC="-c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p -r 24 -c:a aac -ar 48000 -ac 2"
VF="scale=1280:720,setsar=1,fps=24"
n=0; : > $W/list.txt
seg(){ # file ss to [extra_vf]
  n=$((n+1)); local o=$W/$(printf %02d $n).mp4; local x=${4:-}
  ffmpeg -v error -y -ss "$2" -to "$3" -i "$1" -vf "$VF${x:+,$x}" -af aresample=48000 $ENC "$o"
  echo "file '$(basename $o)'" >> $W/list.txt; }
black(){ n=$((n+1)); local o=$W/$(printf %02d $n).mp4
  ffmpeg -v error -y -f lavfi -i color=black:s=1280x720:r=24 -f lavfi -i anullsrc=r=48000:cl=stereo -t "$1" $ENC "$o"
  echo "file '$(basename $o)'" >> $W/list.txt; }
still(){ n=$((n+1)); local o=$W/$(printf %02d $n).mp4
  ffmpeg -v error -y -loop 1 -i "$1" -f lavfi -i anullsrc=r=48000:cl=stereo -t "$2" -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=24" $ENC "$o"
  echo "file '$(basename $o)'" >> $W/list.txt; }

# ПРОХОД 1 — явь
seg $T/SH010_take1.mp4 0 6.0
seg $T/SH020_take2.mp4 0 6.0
seg $T/SH030_take2.mp4 0 6.0
seg $T/SH040_take1.mp4 0 2.8                                   # реле ≈1,6 с
still ../00_bible/approved/SH040_eye_insert_centered.png 0.4    # глаз — match cut по форме
seg $T/SH040_take1.mp4 3.2 4.2 "fade=out:st=0.4:d=0.6"
black 0.5
# ПРОХОД 2 — сдвиг
seg $T/SH050_take1.mp4 0 6.0
seg $T/SH060_take3.mp4 0 6.0
seg $T/SH070_take3.mp4 0 6.0 "fade=out:st=5.2:d=0.8"           # match cut по тени
seg $T/SH080_take2.mp4 0 5.6                                    # луч на пустой полке
black 0.167                                                     # фонарик мигнул
# ПРОХОД 3 — паника
seg $T/SH090_take1.mp4 0.7 2.3
seg $T/SH100_take1.mp4 0 2.0
seg $T/SH100a_take1.mp4 0.30 0.55                               # тапок слетает
seg $T/SH100a_take1.mp4 1.6 2.2                                 # тапок лежит
seg $T/SH100_take1.mp4 2.15 4.0                                 # эллипсис
seg $T/SH100_take1.mp4 4.15 5.45
black 0.3                                                       # фонарик погас
seg $T/SH110a_take1.mp4 0 4.0                                   # хвост — смаз разворота
seg $T/SH110b_take1.mp4 1.40 1.567 "gblur=sigma=40:sigmaV=0.5"  # приземление whip
seg $T/SH110b_take1.mp4 1.567 3.0
black 0.125                                                     # мигание: он исчез
seg $T/SH115_take1.mp4 0 2.2
seg $T/SH120_take1.mp4 0 3.8
seg $T/SH125_take1.mp4 0 5.0
seg $T/SH130_take1.mp4 0 6.0
# SH135 → наплыв 3 с → SH140 (часы 03:06 → 03:07 на 5,6 с) → чёрное
n=$((n+1)); o=$W/$(printf %02d $n).mp4
ffmpeg -v error -y -ss 0 -to 6.0 -i $T/SH135_take1.mp4 -ss 0 -to 5.8 -i $T/SH140_take1.mp4 \
  -i $W/clock_0306.png -i $W/clock_0307.png -filter_complex "\
[0:v]$VF[a];[1:v]$VF[b0];\
[b0][2:v]overlay=644:182:enable='lt(t,5.6)'[b1];[b1][3:v]overlay=644:182:enable='gte(t,5.6)'[b];\
[a][b]xfade=transition=fade:duration=3:offset=3[v];\
[0:a]aresample=48000[a0];[1:a]aresample=48000[a1];[a0][a1]acrossfade=d=3[aout]" \
  -map "[v]" -map "[aout]" $ENC "$o"
echo "file '$(basename $o)'" >> $W/list.txt
black 1.0                                                       # SMASH CUT в чёрное

ffmpeg -v error -y -f concat -safe 0 -i $W/list.txt -c copy ../07_montage/0306_roughcut_v1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 0306_roughcut_v1.mp4
