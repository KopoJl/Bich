# Раскадровка «Последняя дверь» — 8 шотов, 45.0 с, **9:16**, 720p, 24 fps

Версия 2: формат сменён с 16:9 на 9:16 (решение пользователя). Вся геометрия пересчитана по A.17: кадр на сенсоре 20.25 × 36 мм, d = H·f / (0.36·P), наклон на трети θ = atan(6/f), горизонтальный угол 2·atan(10.125/f). Ступени FOV для видео (S.4) не меняются: это диагональ, она одинакова в 16:9 и 9:16.

## Что меняет вертикаль
- **Ширина кадра меньше вдвое:** двое детей рядом в полный рост уже не помещаются. Отношения строятся **глубиной и этажами**: один ближе, другой дальше; одно лицо внизу, другое вверху.
- **Дверь — естественная вертикаль.** Щель двери в SH010 и коридор в SH030 в вертикали работают лучше, чем в 16:9.
- **Безопасная зона Shorts/Reels/TikTok:** главное выше 33% высоты от низа и левее 85% ширины. Нижнюю треть закрывают подпись и кнопки. Для каждого шота ниже посчитано, где главная точка.
- Карты персонажей, реквизита и локаций остаются 16:9: это референсы места и внешности, а не кадры. В 16:9 на листе больше информации. Кадры (Start Frame, клипы) — 9:16.

## Бриф
- Цель, настроение, палитра, Light Lock — без изменений (`00_bible/style_lock.md`).
- Ось 180°: на станции линия «Уилла ↔ дверь», камера на стороне платформы; в детской линия «Уилла ↔ Пип/кровать». В вертикали горизонтальных пробегов почти нет, поэтому направление держится в основном взглядом.
- STRUCTURE / HOOK — `01_script/script.md` (хук в первые 2 с: щель двери, её рука на его запястье, кораблик).
- Блокаут не нужен по умолчанию (стратегия A: карты + Start Frame для SH010).

## Shot list

| SH | Время | Длит. | План | Объектив / FOV | Высота, наклон | Движение | Склейка OUT (тип · ориентир) |
|---|---|---|---|---|---|---|---|
| 010 | 0.0–7.0 | 7.0 | **мультишот v2:** A через плечо (0–2.8) · B снизу на лицо (2.8–4.8) · C у воды (4.8–7.0) | 50 мм/47° · 50 мм/47° · 24 мм/84° | 1.0 · 0.75 · 0.23 м | handheld · статика · статика | HARD CUT на ударе двери → SH020 (её ладони бьют в кафель) |
| 020 | 7.0–12.0 | 5.0 | WS сверху | 28 мм / 63° | 1.6 м, 12.1° вниз | статика | HARD CUT на действии · первый шаг |
| 030 | 12.0–17.0 | 5.0 | MLS со спины, коридор | 35 мм / 63° | 1.0 м, 9.7° вниз | follow 3 км/ч | HARD CUT на действии · порог |
| 040 | 17.0–23.0 | 6.0 | MLS двоих, дверь сверху в глубине | 35 мм / 63° | 1.0 м, 9.7° вниз | статика | HARD CUT по взгляду · вниз на подушку |
| 045 | 23.0–28.0 | 5.0 | два лица этажами | 50 мм / 47° | 0.70 м, 6.8° вниз | статика + перевод фокуса | HARD CUT на действии · рука Пипа |
| 050 | 28.0–34.0 | 6.0 | ECU рук сверху | 85 мм / 29° | 1.0 м, 35° вниз | статика | MATCH CUT · пальцы с корабликом в той же точке |
| 060 | 34.0–40.0 | 6.0 | ладонь → лицо | 50 мм / 47° | 0.9 м, 25° → 6.8° вниз | tilt вверх за 2 с | DISSOLVE 1 с · глаза → глаза |
| 070 | 40.0–45.0 | 5.0 | MCU двоих этажами | 50 мм / 47° | 0.8 м, 6.8° вниз | статика | FADE 1 с |

Сумма 7+5+5+6+5+6+6+5 = 45.0 с ✓ (SH010 удлинён до 7 с, SH050 сокращён до 6 с). Генерация каждого шота на 1 с длиннее (целые секунды, Seedance 2.5: 4–30 с).

## GEOMETRY (9:16)

```
GEOMETRY SH010 — v2, три сегмента: см. 03_prompts/SH010_keyframes.md (A over-the-shoulder 1.0 м/50 мм, B low-angle 0.75 м/50 мм, C ground-level 0.23 м/24 мм). Версия v1 (один общий план) отклонена — разбор в 00_bible/pro_method.md.
```
```
GEOMETRY SH020
INTENT: small and pressed — the station swallows her, the door is gone
CAMERA: height 1.6 m · lens 28 mm · tilt 12.1° down
HEROES: Willa head 1.30 m (standing) at 3.4 m
RESULT: head below horizon (1.6 > 1.30) · horizon on the upper third line
SIZE: small = 30% at 3.4 m (1.30·28/(0.36·30) = 3.37)
THIRDS: Willa in the center-left, back to camera, facing the wall · the boat lights up 1 m to her right and drifts along the wall into depth, at 4.5 m it sits at ≈38% height · open space up and right
SAFE ZONE: Willa ≈40–70%, boat 38% ✓
CHECK: yes
```
```
GEOMETRY SH030
INTENT: determined — she moves forward on her own will
CAMERA: height 1.0 m · lens 35 mm · tilt 9.7° down · follows 2.5 m behind
HEROES: Willa head 1.30 m (wading)
RESULT: head above horizon (1.30 > 1.0) · horizon on the upper third line
SIZE: medium = 50% at 2.5 m (1.30·35/(0.36·50) = 2.53)
THIRDS: Willa centered (the passage converges on the door — deliberate center) · door at the vanishing point, upper third · boat ahead of her at ≈40%
SAFE ZONE: ✓
CHECK: yes
```
```
GEOMETRY SH040
INTENT: small and powerless — two kids in a dark room
CAMERA: height 1.0 m · lens 35 mm · tilt 9.7° down · corner by the window, diagonal to the door
HEROES: Willa 1.30 m at the door (5 m) → kneeling, head 0.95 m at 2.05 m · Pip sitting, head 0.70 m at 2.05 m
RESULT: after she kneels both heads below the horizon (1.0) · horizon on the upper third line
SIZE: Willa kneeling medium = 45% at 2.05 m (0.95·35/(0.36·45) = 2.05); frame width at 2.05 m ≈ 1.2 m — they sit shoulder to shoulder
THIRDS: the door in the upper third (her entry) · Willa's head at 65%, Pip's at 53% · her hand on his shoulder at ≈50%
SAFE ZONE: ✓
CHECK: yes
```
```
GEOMETRY SH045
INTENT: equal — she meets herself
CAMERA: height 0.70 m · lens 50 mm · tilt 6.8° down · beside the nightstand at the bed head
HEROES: sleeping Willa head on the pillow 0.62 m at 0.6 m · ghost Willa eyes 0.85 m (kneeling) at 1.5 m
RESULT: horizon on the upper third line; the ghost's eyes above it — she looks down at herself
SIZE: sleeping face large in the lower half; ghost face medium close-up in the upper part
THIRDS: sleeping face center ≈48% height · ghost eyes ≈82% height, upper third · two identical gold star clips stacked in one frame
SAFE ZONE: ✓
CHECK: yes
```
```
GEOMETRY SH050
INTENT: detail — his hands tell the story
CAMERA: height 1.0 m · lens 85 mm · tilt 35° down onto the quilt (0.55 m)
RESULT: no horizon
SIZE: her open palm and the 12 cm boat fill 60% of the frame width
THIRDS: her palm at ≈40% height center · his hands enter from the top
SAFE ZONE: ✓
CHECK: yes
```
```
GEOMETRY SH060
INTENT: inward — the decision is hers
CAMERA: height 0.9 m · lens 50 mm · tilt 25° down on her palm (0.70 m), tilts up to 6.8° down on her face
HEROES: ghost Willa kneeling, eyes 0.85 m at 1.2 m · Pip soft in the background, head 0.65 m on the bed edge
RESULT: end — her eyes just under the camera height, horizon on the upper third line
SIZE: start — palm in the same screen spot as the end of SH050 (≈40% height, center); end — close-up
THIRDS: end — her eyes at ≈61% height · Pip soft lower left
SAFE ZONE: ✓
CHECK: yes
```
```
GEOMETRY SH070
INTENT: equal — finally eye to eye
CAMERA: height 0.8 m · lens 50 mm · tilt 6.8° down · beside the bed
HEROES: Willa head on the pillow 0.62 m at 1.0 m (lower) · Pip head 0.65 → 0.80 m at 1.4 m (upper)
RESULT: Pip's eyes reach the horizon, Willa looks up at him — he is the one who brought her back
SIZE: medium close-up of both, stacked
THIRDS: Willa's face ≈41% · Pip's face ≈67% · joined hands with the boat ≈32% (end frame: boat star catches the nightlight)
SAFE ZONE: faces ✓; hands on the edge of the zone — the final hold lasts 1.5 s, the caption usually appears later
CHECK: yes
```

## Карточки панелей (сжато)

**SH010 | хук** · IDEA: зритель уверен, что она спасает его. · MASSES: тёмная холодная станция, яркая тёплая вертикальная полоса щели. · FOCAL: её хват на его запястье + белый кораблик в тёплом свете. · LINES: щель — вертикаль через весь кадр; её рука — диагональ от лица к щели. · POWER: равны. · CUT OUT: ладонь бьёт в закрытую дверь.

**SH020 | двери нет** · IDEA: сила не работает. · FOCAL: её удары → загорающийся кораблик (самая тёплая точка). · CUT OUT: первый шаг.

**SH030 | за корабликом** · IDEA: надежда. · LINES: коридор сходится к двери, полоска тёплого света под ней. · END: её силуэт в тёплом проёме.

**SH040 | рука насквозь** · IDEA: перелом тактики силы. · MASSES: тёплое пятно ночника на Пипе и корабликах; Уилла в холодном голубом. · FOCAL: её рука на его плече; кардиган не мнётся. · CUT OUT: взгляд вниз-влево на подушку.

**SH045 | узнавание** · IDEA: «это я». · FOCAL: две одинаковые заколки-звезды одна над другой. · MOVE: фокус с призрака (верх) на спящую (низ).

**SH050 | его руки** · IDEA: он делает это не первый раз. · SECONDARY: закатывает рукав. · CUT OUT: MATCH — сомкнутые пальцы.

**SH060 | решение** · IDEA: перестать тянуть, принять. · FOCAL: кораблик → её глаза → закрытые глаза.

**SH070 | глаза в глаза** · IDEA: дома. · FOCAL: их взгляды; финал — кораблик со звездой в сцепленных руках.

## Последовательность
- Нарастание: средние и общие в хуке → крупные в раскрытии; MATCH CUT потрачен один раз.
- Через склейки внимание держится в центре вертикали: ладонь → ладонь, шаг → шаг, порог → порог, взгляд → подушка, рука → рука.

## Карта ракурсов (библиотека shoootai camera-angles) — ни один не повторяется
| Шот | Ракурс | Зачем этот |
|---|---|---|
| SH010-A | Hip-Level Shot, front three-quarter | читаем всё событие: дверь, узкая щель, она держит, он за щелью |
| SH010-B | Through-an-Opening View — обратная точка из комнаты, через щель | его сторона: рука с корабликом на переднем плане, её лицо за щелью не берёт подарок |
| SH010-C | Split-Level Waterline View | граница миров: над водой дверь захлопнулась, под водой её сапоги; кораблик ровно на линии воды |
| SH020 | High-Angle Shot (35° вниз) | она мала, стены нет, сила не работает |
| SH030 | Rear Three-Quarter View (follow) | идём за ней за корабликом |
| SH040 | High Corner View | двое в тёмной комнате, она бессильна |
| SH045 | Over-the-Shoulder (через плечо призрака) | она смотрит на себя спящую |
| SH050 | Top-Down Shot | руки: кораблик ложится в ладонь |
| SH060 | Eye-Level Shot | решение — наравне со зрителем |
| SH070 | Side Profile View | двое в профиль глаза в глаза |
