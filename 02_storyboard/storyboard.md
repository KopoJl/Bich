# «03:06» — бриф и раскадровка

## A. Бриф

| | |
|---|---|
| Цель | короткий хоррор-мультфильм ≈ 98 с; зритель должен почувствовать, что граница между «мне кажется» и «оно здесь» стёрлась |
| Формат | 16:9 · 1920×1080 · 24 fps · модель по умолчанию Seedance 2.x, клипы 5–9 с |
| Настроение | изоляция, сдержанный страх, горе; паранормальное выглядит так же буднично, как быт |
| Палитра | 60 % `#2B3640` · 30 % `#55574F` / `#3E4A3B` · 10 % `#D79A3E` (см. `00_bible/style_lock.md`) |
| Ось 180° | Рут ↔ северная стена (дверь, часы, шкаф). Камера на восточной стороне, со стороны окна. Рут смотрит на угрозу вглубь кадра или вправо; угроза справа или в глубине |
| Light Lock | лампа на левом конце столика, 2700K, снизу и спереди · ртутный фонарь за эркером справа, 6500K · key:fill 6:1 · WB 4000K |
| STRUCTURE | №9 «Временная петля»: три прохода одной ночи (подробно в `01_script/script.md`) |
| HOOK | информационный разрыв + in medias res: 0,3 с — её шёпот «Three-oh-six. The house is quiet.», щель двери в глубине |

Расчёты геометрии: 16:9, сенсор 36 мм; d = H · f / (0,2025 · P); наклон для горизонта на трети: 24 мм 8,0° · 28 мм 6,9° · 35 мм 5,5° · 50 мм 3,9° · 85 мм 2,3°. Рут сидя: макушка 1,25 м, глаза 1,13 м; стоя: 1,65 / 1,53 м. Жилец: 2,3 м, сутулясь в проёме — 1,95 м.

## B. Shot list

| № | Время | План | Объектив | Ракурс / h камеры | Камера | Длит. | Склейка на выходе (тип · ориентир) |
|---|---|---|---|---|---|---|---|
| SH010 | 0–6 | ECU магнитофон | 50 мм | ниже глаз, 0,62 м | статика | 6 | HARD CUT · щелчок кнопки STOP |
| SH020 | 6–14 | WS комната | 24 мм | высокий, 1,6 м | пролёт сквозь лучи, 1,0 м | 8 | HARD CUT на действии · скрип сверху, голова начинает поворот |
| SH030 | 14–22 | OTS → дверной проём | 35 мм | уровень глаз, 1,2 м | медленный зловещий наезд, 0,6 м | 8 | HARD CUT · щелчок реле часов |
| SH040 | 22–28 | ECU часы + вставка глаза | 85 мм | 1,9 м | статика | 6 | J-CUT · её записанный голос за 1,0 с до SH050 |
| SH050 | 28–36 | MS Рут из щели шкафа | 28 мм | высокий, 1,7 м, голландский 5° | подглядывающая панорама 10° | 8 | HARD CUT на действии · палец на PLAY |
| SH060 | 36–43 | CU лицо | 50 мм | 1,3 м | спуск из тьмы потолка к лицу | 7 | J-CUT · треск винила за 0,8 с |
| SH070 | 43–51 | WS сверху | 24 мм | под потолком 2,35 м, голландский 8° | парящий дрейф, 1,2 м | 8 | MATCH CUT по тени · спина Рут закрывает кадр |
| SH080 | 51–59 | OTS → шкаф | 35 мм | 1,45 м | слепой наезд во тьму, 1,0 м | 8 | SMASH CUT · щелчок фонарика |
| SH090 | 59–60,5 | ECU Жилец в шкафу | 85 мм | снизу, 1,45 м | статика | 1,5 (генерация 4) | SMASH CUT · звук обрывается |
| SH100 | 60,5–66,5 | MS со спины, коридор | 28 мм | 1,5 м | паническая ручная за лучом | 6 | MATCH CUT по тени · луч уходит, чернота |
| SH110 | 66,5–71,5 | MCU → WS проём | 35 мм | 1,5 м | whip pan 180° | 5 | HARD CUT на действии · приземление на Жильце |
| SH120 | 71,5–79,5 | MS снизу, Жилец | 24 мм | 1,0 м, голландский 12° | облёт 90° с контровым светом | 8 | HARD CUT · визг ленты |
| SH130 | 79,5–84,5 | CU руки | 50 мм | 0,9 м | статика | 5 | HARD CUT на действии · лента рвётся |
| SH135 | 84,5–90,5 | MCU лицо | 50 мм | 1,3 м | статика | 6 | SLOW DISSOLVE 3 с по фактуре · лицо → обои → рассвет |
| SH140 | 90,5–98,5 | WS комната, рассвет | 24 мм | 1,6 м | статика | 8 | SMASH CUT в чёрное · щелчок реле |

Нарастание (B.18.10): проход 1 — ровный горизонт, движения ≤ 0,45 км/ч; проход 2 — завал 5° → 8°, камера отрывается от пола; проход 3 — 12°, ручная камера и whip. Самый сильный удар (smash на глаз в шкафу) один раз, на 59-й секунде, около 60 % хронометража.

---

## Геометрия и карточки панелей

### SH010 — хук
```
GEOMETRY SH010
INTENT: equal — object as the hero; we sit at table height beside the machine
CAMERA: height 0.62 m · lens 50 mm · tilt 3.9° down · at (2.0; 3.0) looking NW
SUBJECT: recorder top 0.55 m (table 0.45 + 0.10) · hall door gap 0–2.0 m, 2.31 m away
RESULT: recorder below horizon (0.55 < 0.62) · horizon on the upper third line
SIZE: recorder 0.30 m wide = ~52% of frame width at 0.8 m (frame width 0.58 m at 40° horizontal)
THIRDS: recorder on the lower-left intersection · black door gap on the upper-right intersection · open space right
CHECK: yes
```
`PANEL 1 | beat: the night is logged | 6 s` · IDEA: тишина как улика; что-то не так, но непонятно что · intensity low · POV: Рут.
LEAVE OUT: лицо Рут (только голос и правая рука) · MASSES: тёплое пятно лампы слева, правая половина в синей тьме · FOCAL: красный огонёк REC против чёрной щели · SCREEN DIRECTION: рука входит слева · CUT OUT: щелчок STOP → SH020.

### SH020 — пролёт сквозь лучи (Кон: подсмотренный быт)
```
GEOMETRY SH020
INTENT: small and pressed (lightly) — a woman alone in a big dark room
CAMERA: height 1.6 m · lens 24 mm · tilt 8.0° down · truck from (3.7; 0.3) to (3.7; 1.3), looking NW
HEROES: Ruth head 1.25 m (sitting)
RESULT: Ruth head below horizon (1.6 > 1.25) · horizon on the upper third line
SIZE: medium = 52.9% of frame height at 2.8 m (1.25·24/(0.2025·2.8))
THIRDS: Ruth on the left third · her head on the upper-left intersection · light shafts on the right third · open space right (window)
CHECK: yes
```
Камера идёт вдоль эркера на север 1,0 м за 8 с (0,45 км/ч), перпендикулярно трём лучам. Тени рамы эркера скользят по ковру, в лучах висит пыль. Рут неподвижна, пьёт чай, перед ней работает магнитофон. CUT OUT: скрип половицы над головой, её голова начинает поворот.

### SH030 — медленный зловещий наезд на дверь
```
GEOMETRY SH030
INTENT: equal — we look with her, over her right shoulder
CAMERA: height 1.2 m · lens 35 mm · tilt 5.5° down · from (1.95; 2.25) push 0.6 m toward the hall door
HEROES: Ruth head 1.25 m (sitting), back of head in the foreground
RESULT: her crown just above the horizon (1.25 vs 1.2) · horizon on the upper third line
SIZE: door gap 2.96 m → 2.36 m away; the black gap grows from ~12% to ~16% of frame width
THIRDS: her head on the right third (soft) · door gap on the left third · focal point: the black gap
CHECK: yes
```
Наезд 0,6 м за 8 с (0,27 км/ч), «неестественно медленный»: никакой тряски, без ускорения. Рут шепчет «Pipes.» и не отводит глаз от проёма. CUT OUT: щелчок реле.

### SH040 — 03:07 и вставка глаза
```
GEOMETRY SH040
INTENT: unjustified symmetry — the clock as a face
CAMERA: height 1.9 m (clock centre) · lens 85 mm · tilt 0° · 2.1 m from the clock
RESULT: horizon through the clock centre, frame centred by design (B.18.8)
SIZE: clock Ø 0.30 m = ~60% of frame height
INSERT 0.4 s: ECU round pale eye in the cupboard gap, its centre at the same screen point as the clock centre (match cut on shape)
CHECK: yes
```
0–3 с минутная стрелка дрожит; 3,0 с реле щёлкает, стрелка встаёт на 03:07; 3,2–3,6 с вставка глаза; 3,6–4,6 с лампа мигает трижды и гаснет; 4,6–6,0 с чёрный, с 5,0 с звучит её записанный голос (J-cut).

### SH050 — подглядывание из шкафа (проход 2)
```
GEOMETRY SH050
INTENT: small and pressed — watched from inside the cupboard
CAMERA: height 1.7 m · lens 28 mm · tilt 6.9° down · Dutch 5° clockwise · at the cupboard gap (2.9; 4.9) looking SW
HEROES: Ruth head 1.25 m (sitting)
RESULT: Ruth head below horizon (1.7 > 1.25) · horizon on the upper third line
SIZE: large = 65.5% of frame height at 2.64 m
THIRDS: cupboard door edge blurred over the right 25% of frame · Ruth on the left third · eyes on the upper third line
CHECK: yes
```
Панорама 10° влево вслед за её рукой к чашке. Чай опять горячий, на счётчике снова 03:06. Её взгляд уходит в кадре вправо, мимо камеры, на часы. Ось держится: камера на восточной половине северной стены.

### SH060 — спуск из тьмы к лицу
```
GEOMETRY SH060
INTENT: small and pressed — the dark ceiling weighs on her
CAMERA: height 1.3 m · lens 50 mm · tilt from 60° up to 3.9° down over 7 s · at (2.3; 3.2), 0.92 m from her face
HEROES: Ruth eyes 1.13 m (sitting)
RESULT: her eyes below horizon (1.3 > 1.13) · horizon on the upper third line in the end frame
SIZE: CU, face ~70% of frame height
THIRDS: face on the left third · eyes on the upper third line · lamp just out of frame on the right, below her chin
CHECK: yes
```
Она слушает запись, наклонившись к магнитофону. На плёнке её голос и под ним второй шёпот. Шёпот уходит из левого уха за спину (это делается на монтаже).

### SH070 — парящая камера
```
GEOMETRY SH070
INTENT: small and pressed — a presence under the ceiling
CAMERA: height 2.35 m · lens 24 mm · tilt 50° down · Dutch 8° · drift from (2.6; 4.4) to (2.0; 3.4), 1.17 m over 8 s (0.53 km/h)
HEROES: Ruth head 1.25 m (sitting → standing 1.65 m at 6 s)
RESULT: Ruth far below horizon in both poses
SIZE: medium-large = 73% at 2.03 m (sitting)
THIRDS: Ruth lower-left · record player and crucifix shadow on the left wall, upper-left third
CHECK: yes
```
Проигрыватель сам опускает иглу, детская песенка звучит замедленно. Тень распятия на западной стене вытягивается вверх на 2–3 своих длины, хотя лампа неподвижна. Рут правой рукой берёт фонарик со столика, встаёт (6,0 с) прямо в объектив, спина закрывает кадр.

### SH080 — слепой наезд в шкаф
```
GEOMETRY SH080
INTENT: equal → swallowed — we walk with her into the dark
CAMERA: height 1.45 m · lens 35 mm · tilt 0° · from (1.9; 3.0) push 1.0 m toward the cupboard gap (0.45 km/h)
HEROES: Ruth head 1.65 m (standing), her back fills frame at 0 s and slides out to the left by 1.5 s
RESULT: her head above horizon (1.65 > 1.45), we never see her face
SIZE: cupboard gap (open 15 cm) grows from ~10% to ~25% of frame width
THIRDS: black gap on the centre — the strongest dark mass, 65% of frame in shadow
CHECK: yes
```
5,0 с — все бытовые звуки обрываются (мёртвая тишина). 6,0 с — лампа гаснет. 7,8 с — щелчок фонарика → SMASH CUT.

### SH090 — smash
```
GEOMETRY SH090
INTENT: the Lodger dominates
CAMERA: height 1.45 m · lens 85 mm · tilt 6° up · 1.0 m from his folded head (1.85 m)
RESULT: his head above horizon (1.85 > 1.45)
SIZE: ECU — head and shoulder fill the frame
CHECK: yes
```
Голова сложена под 80°, луч фонарика касается мокрого плеча, лицо остаётся тёмным, загорается круглый бледный глаз. Удар диссонирующих скрипок, затем провал звука. Генерировать 4 с, в монтаж взять 1,5 с.

### SH100 — паника в коридоре
```
GEOMETRY SH100
INTENT: equal — we run with her
CAMERA: handheld at 1.5 m · lens 28 mm · tilt 0° · following 3.0 m behind her at 9 km/h
HEROES: Ruth head 1.65 m (running)
RESULT: her head just above horizon (1.65 > 1.5)
SIZE: large = 76% at 3.0 m
THIRDS: Ruth on the centre-left, torch beam leads to the right third, the frame jerks after the beam
CHECK: yes
```
Эллиптический монтаж: вырезать по 3–4 кадра на 2,0 с и на 4,0 с. Луч уходит вниз, на щиток, коридор чернеет → match cut по тени.

### SH110 — whip pan
```
GEOMETRY SH110
INTENT: equal (her) → the Lodger dominates (end)
CAMERA: height 1.5 m · lens 35 mm · whip 180° from her face to the front-room doorway 4.2 m away
HEROES: Ruth head 1.65 m (standing) · Lodger head 1.95 m (stooped in the 2.0 m doorway)
RESULT: both heads above horizon; his higher — he dominates
SIZE: Lodger large = 80.2% at 4.2 m (1.95·35/(0.2025·4.2))
THIRDS: Lodger on the centre (doorway frames him) — a frame in a frame
CHECK: yes
```
0–2,2 с: она дёргает рубильник, света нет. 2,2 с: громко из комнаты её голос с плёнки «Three-oh-six». 2,6–3,4 с: whip 0,8 с со смазом. 3,4–5,0 с: проём, в нём сутулый Жилец, контровой синий свет из эркера.

### SH120 — облёт силуэта
```
GEOMETRY SH120
INTENT: the Lodger dominates and does not fit the frame
CAMERA: height 1.0 m · lens 24 mm · Dutch 12° · orbit 90° at radius 1.6 m around him (2.2; 3.9), from SW (1.07; 2.77) to W (0.6; 3.9)
HEROES: Lodger head 2.3 m (upright, 0.2 m under the ceiling)
RESULT: his head far above horizon (2.3 > 1.0)
SIZE: 170% of frame height at 1.6 m — the crown is cut by the top edge on purpose (B.18.6)
THIRDS: his long fingers on the recorder's PLAY key on the lower third · the window behind him lights only his outline
CHECK: yes
```
Контровой свет перетекает по силуэту с правого края на левый. С плёнки её голос замедляется и опускается в тот самый шёпот: это она сама.

### SH130 — руки и лента
```
GEOMETRY SH130
CAMERA: height 0.9 m · lens 50 mm · tilt 25° down · 0.6 m from the recorder
RESULT: table and hands below horizon · CU hands fill the lower two thirds
CHECK: yes
```
0,5 с: она роняет фонарик, луч крутится по полу. Левая рука жмёт EJECT, правая вынимает кассету, указательный палец цепляет ленту и тянет её петлями. 4,5 с: визг ленты, звук обрывается.

### SH135 — лицо → обои
```
GEOMETRY SH135
CAMERA: height 1.3 m · lens 50 mm · tilt 3.9° down · 0.9 m from her face
HEROES: Ruth eyes 1.13 m (sinking back into the armchair)
RESULT: eyes below horizon · horizon on the upper third line
THIRDS: face on the right third, looking screen-left at the crucifix wall — the first look away from the threat
CHECK: yes
```
Возвращаются звуки быта (дождь, реле) — сущность ушла. С 3,0 с медленный наплыв: лицо → отходящий шов обоев с распятием → рассвет.

### SH140 — рассвет (рифма с SH020)
```
GEOMETRY SH140
INTENT: small and pressed (lightly) — the same as SH020, the loop
CAMERA: height 1.6 m · lens 24 mm · tilt 8.0° down · static at (3.7; 0.8)
HEROES: Ruth head 1.25 m (asleep in the armchair)
RESULT: head below horizon · horizon on the upper third line
SIZE: medium = 52.9% at 2.8 m
THIRDS: Ruth left third · clock 03:06 on the upper third line · cupboard gap 4 cm on the right third
CHECK: yes
```
Серый пасмурный свет; за тюлем проезжает красный даблдекер, его красный бок отражается в стекле. Петли ленты лежат на ковре. 7,5 с щёлкает реле → SMASH CUT в чёрное.
