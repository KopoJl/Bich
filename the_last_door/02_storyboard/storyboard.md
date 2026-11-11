# Раскадровка «Последняя дверь» — 8 шотов, 45.0 с, 16:9, 720p, 24 fps

## Бриф
- Цель: за 45 с перевернуть смысл первого кадра без единого слова.
- Настроение: хук — физическая борьба (интенсивность 4); раскрытие — тишина и сдержанность (интенсивность 2).
- Палитра и Light Lock — `00_bible/style_lock.md`. Холод = потерянность, тепло = дом.
- Ось 180°: на станции — линия «Уилла ↔ дверь», камера на стороне платформы; Уилла смотрит и движется вправо по экрану (к дому). В детской — линия «Уилла ↔ Пип/кровать»: Уилла справа смотрит влево, кровать и Пип слева.
- STRUCTURE / HOOK — `01_script/script.md`.
- Блокаут: **не нужен по умолчанию** — нет сложных пролётов и массовки. Стратегия A: карты + Start Frame там, где сложная расстановка (SH010). Если SH030 (follow) плывёт по камере — блокаут в режиме «Кубы» только для него.

## Shot list

| SH | Время | Длит. | План | Объектив / FOV | Ракурс, высота | Движение камеры | Склейка OUT (тип · ориентир) |
|---|---|---|---|---|---|---|---|
| 010 | 0.0–6.0 | 6.0 | FS | 35 мм / 63° | на уровне детей, 1.0 м, наклон 5.5° вниз | дрейфующий handheld | HARD CUT на действии · ладонь бьёт в закрытую дверь → ладонь бьёт в кафель; звук удара мостом |
| 020 | 6.0–11.0 | 5.0 | WS | 28 мм / 63° | сверху, 1.6 м, 6.9° вниз | статика | HARD CUT на действии · первый шаг Уиллы вправо |
| 030 | 11.0–16.0 | 5.0 | MS→MLS (follow) | 35 мм / 63° | 1.0 м, 5.5° вниз | follow сзади 3 км/ч | HARD CUT на действии · дверь распахивается, Уилла переступает порог (обратная точка) |
| 040 | 16.0–22.0 | 6.0 | MLS | 35 мм / 63° | 1.0 м, 5.5° вниз | статика | HARD CUT по взгляду · её глаза уходят влево на подушку |
| 045 | 22.0–27.0 | 5.0 | CU двух лиц | 50 мм / 47° | 0.75 м, 0° | статика + перевод фокуса | HARD CUT на действии · рука Пипа входит в кадр к ладони |
| 050 | 27.0–34.0 | 7.0 | ECU рук | 85 мм / 29° | 1.0 м, 35° вниз | статика | MATCH CUT · сомкнутые пальцы с корабликом в той же точке экрана |
| 060 | 34.0–40.0 | 6.0 | CU ладонь → лицо | 50 мм / 47° | 0.9 м | медленный tilt вверх 15° за 2 с | DISSOLVE 1 с · закрытые глаза призрака → закрытые глаза спящей |
| 070 | 40.0–45.0 | 5.0 | MCU двоих | 50 мм / 47° | 0.8 м, 0° | статика | FADE to black 1 с |

Сумма: 6+5+5+6+5+7+6+5 = 45.0 с ✓. Каждый шот генерируется на 1 с длиннее (запас 0.5 с с краёв, склейки плавают на ±0.5 с — S.11).

## GEOMETRY (16:9, сенсор 36 мм, d = H·f / (0.2025·P))

```
GEOMETRY SH010
INTENT: equal — two kids in an equal tug-of-war, viewer at their height
CAMERA: height 1.0 m · lens 35 mm · tilt 5.5° down
HEROES: Willa head 1.20 m (leaning back, knees bent) · Pip head 1.10 m (standing, on tiptoe up to 1.15)
RESULT: both heads just above the horizon (1.0 m) — equal force · horizon on the upper third line
SIZE: Willa large = 80% of frame height at 2.6 m (1.20·35/(0.2025·80) = 2.59)
THIRDS: Willa on the left third · Pip in the door gap on the right third · eyes on the upper third line · focal point = her grip on his wrist + the boat, upper-right intersection · open space between them
CHECK: yes
```
```
GEOMETRY SH020
INTENT: small and pressed — the station swallows her, the door is gone
CAMERA: height 1.6 m · lens 28 mm · tilt 6.9° down
HEROES: Willa head 1.30 m (standing)
RESULT: head below horizon (1.6 > 1.30) · horizon on the upper third line
SIZE: small = 30% at 6.0 m (1.30·28/(0.2025·30) = 5.99); floor visible from 3.2 m → boat placed 3.5 m from camera
THIRDS: Willa on the left third, back to camera, facing the wall · boat lower-right intersection · open space right (where she will go)
CHECK: yes
```
```
GEOMETRY SH030
INTENT: determined — she moves forward on her own will
CAMERA: height 1.0 m · lens 35 mm · tilt 5.5° down · follows 4.5 m behind
HEROES: Willa head 1.30 m (wading)
RESULT: head above horizon (1.30 > 1.0) · horizon on the upper third line
SIZE: medium = 50% at 4.5 m (1.30·35/(0.2025·50) = 4.49)
THIRDS: Willa centered in the passage (the passage lines converge on the door, deliberate center) · glowing boat ahead on the lower third · door at the vanishing point
CHECK: yes
```
```
GEOMETRY SH040
INTENT: small and powerless — two kids in a dark room, she cannot change anything
CAMERA: height 1.0 m · lens 35 mm · tilt 5.5° down · corner by the window, diagonal to the door
HEROES: Willa head 1.30 m at the door (5.2 m) → 0.95 m kneeling (3.65 m) · Pip head 0.70 m (sitting on the floor)
RESULT: after she kneels both heads below horizon (1.0 > 0.95, 0.70) · horizon on the upper third line
SIZE: Willa kneeling medium = 45% at 3.65 m (0.95·35/(0.2025·45) = 3.65); at the door 43% at 5.2 m
THIRDS: bed on the left · Pip on the right-center lower third · Willa kneels on the right third, facing screen-left toward Pip and the bed · focal point = her hand on his shoulder
CHECK: yes
```
```
GEOMETRY SH045
INTENT: equal — she meets herself
CAMERA: height 0.75 m · lens 50 mm · tilt 0° · beside the nightstand at the bed head
HEROES: sleeping Willa head on the pillow 0.62 m, 0.6 m from lens · ghost Willa eyes 0.85 m (kneeling), 1.5 m from lens
RESULT: sleeping face below, ghost eyes slightly above the horizon (0.75) — the ghost looks down at herself
SIZE: sleeping face fills the left third in the foreground; ghost face medium close-up on the right third
THIRDS: sleeping face on the left third · ghost eyes on the upper-right intersection · focus pulls from the ghost to the sleeping face
CHECK: yes
```
```
GEOMETRY SH050
INTENT: detail — what his hands do is the whole story
CAMERA: height 1.0 m · lens 85 mm · tilt 35° down onto the quilt
HEROES: hands only (quilt at 0.55 m)
RESULT: no horizon (looking down at the quilt)
SIZE: two child hands and the 12 cm boat fill 60% of the frame width
THIRDS: her open palm on the lower-left intersection · his hands enter from the right
CHECK: yes
```
```
GEOMETRY SH060
INTENT: equal → inward — the decision is hers
CAMERA: height 0.9 m · lens 50 mm · starts tilted 25° down on her palm (0.70 m), tilts up 15° to her face (eyes 0.85 m), ends 10° down
HEROES: ghost Willa kneeling, eyes 0.85 m · Pip in the soft background, head 0.65 m resting on the bed edge
RESULT: her eyes just below the horizon at the end — inward, quiet · horizon on the upper third line at the end
SIZE: start — palm with the boat in the same screen spot as the end of SH050 (match); end — close-up, face 55% of frame height
THIRDS: end — her eyes on the upper third line, right third · Pip soft on the left lower third
CHECK: yes
```
```
GEOMETRY SH070
INTENT: equal — finally eye to eye
CAMERA: height 0.8 m · lens 50 mm · tilt 0°
HEROES: Willa head on the pillow 0.62 m (left) · Pip head 0.65 → 0.80 m (lifts it from the bed edge, right)
RESULT: both eyes near the horizon (0.8) at the end — equal
SIZE: medium close-up of both, faces 30% of frame height each
THIRDS: Willa's eyes on the left third · Pip's eyes on the right third, upper line · joined hands with the boat at the lower center (end frame)
CHECK: yes
```

## Карточки панелей (сжато, B.18.14)

**SH010 | хук | 6.0 с** · IDEA: кто кого спасает — зритель уверен, что она его. Интенсивность высокая. POV Уиллы. · LEAVE OUT: комната за Пипом почти вся засвечена тёплым — видно только край стены со звёздами. · MASSES: тёмная холодная станция, яркая тёплая щель справа. · FOCAL: её хват на его запястье + кораблик в его пальцах (самое контрастное: белая бумага в тёплом свете). · LINES: её тело — длинная диагональ от упора сапог к руке; щель — вертикаль. · POWER: равны, щель между ними — граница миров. · SCREEN: она тянет влево, дверь тянет вправо. · CUT OUT: ладонь бьёт в закрытую дверь → SH020.

**SH020 | двери нет | 5.0 с** · IDEA: сила не работает. Высокая. · MASSES: чернота станции, светлый пятачок кафеля, золотая точка кораблика сзади. · FOCAL: сначала её удары, потом загорающийся кораблик (самая тёплая точка). · SCREEN: кораблик плывёт вправо; она оборачивается через правое плечо. · CUT OUT: первый шаг вправо.

**SH030 | за корабликом | 5.0 с** · IDEA: надежда. Средняя. · LINES: переход сходится к двери, полоска тёплого света под дверью. · MOVE: follow, конечная композиция — её силуэт в тёплом проёме. · CUT OUT: переступает порог.

**SH040 | рука насквозь | 6.0 с** · IDEA: перелом тактики силы. Средняя → тишина. · MASSES: тёплое пятно ночника на Пипе и корабликах; Уилла в холодном голубом свете. · FOCAL: её рука на его плече; кардиган не мнётся, он не оборачивается. · POWER: оба под горизонтом; разный свет — разные миры (B.18.7). · CUT OUT: взгляд влево на подушку.

**SH045 | узнавание | 5.0 с** · IDEA: «это я». Сдержанно (2). · FOCAL: две одинаковые заколки-звезды в одном кадре. · MOVE: фокус с призрака на спящую. · CUT OUT: рука Пипа входит в кадр.

**SH050 | его руки | 7.0 с** · IDEA: он делает это не первый раз. · FOCAL: кораблик ложится в ладонь. · SECONDARY: он закатывает сползающий рукав. · CUT OUT: MATCH — сомкнутые пальцы.

**SH060 | решение | 6.0 с** · IDEA: перестать тянуть, принять. Сдержанно (2). · FOCAL: кораблик → её глаза → закрытые глаза. · CUT OUT: наплыв.

**SH070 | глаза в глаза | 5.0 с** · IDEA: дома. Тихая радость, не улыбка до ушей. · FOCAL: их взгляды; финальный кадр — кораблик со звездой в сцепленных руках. · CUT OUT: затемнение.

## Проверка последовательности (B.18.10–11)
- Нарастание: широкие и средние планы в хуке → крупные в раскрытии; самый сильный приём (MATCH CUT рука-в-руку) потрачен один раз, на повороте.
- Направление: на станции всё движение вправо (к дому); в детской Уилла приходит справа и смотрит влево — встречное направление, «разворот» её пути.
- Внимание через склейки: ладонь → ладонь (010→020); шаг → шаг (020→030); порог → порог (030→040); взгляд → подушка (040→045); рука → рука (050→060).
