# Style Lock, палитра, Light Lock — «Последняя дверь»

Формат: **9:16** (вертикаль, Shorts/Reels/TikTok), 720×1280 (720p), 24 fps, 45 с. Карты персонажей, реквизита и локаций — 16:9 (референсы, не кадры). Видеомодель: Seedance 2.5. Без диалогов, звук SFX + дыхание, музыка на монтаже.

## Выбор стиля (shoootai.com → 3D анимация)

| Стиль | Решение | Почему |
|---|---|---|
| **Expressive Family 3D** | **ВЫБРАН** | Округлые пропорции и крупные глаза держат мимику ребёнка; «believable body structure, consistent limbs, contact shadows, strong silhouette» — прямая опора для веса, силуэта и читаемых поз. Чистые материалы не «ползут» в движении. |
| Painterly Fantasy 3D | нет | Живописная фактура на движущихся героях «ползёт» как наклеенная (B.14); встроенный золотой солнечный свет и индустриальный город спорят с затопленной станцией и детской. |
| Stylized 3D (матовая геометрия) | нет | В промте «restrained posing, avoid excessive cuteness, low contrast» — прямо против преувеличения поз и контраста холод/тепло. |
| Cel-Shaded 3D | нет | Контурные линии и ступенчатые тени мерцают в видеогенерации. |
| Остальные (воксели, фигурка, кубизм, силикон, fashion, маскоты, гротеск) | нет | Не про детей и тихую эмоцию. |

Что я **убрал** из промта сайта и почему:
- `Warm golden backlight, small floating particles and delicate bokeh` — это свет одной сцены, а у нас две противоположные (холодная станция и тёплая детская). Свет живёт в Light Lock.
- `a clear readable emotion` — эмоция словом даёт маску (S.10). Игра задаётся задачей.
- `a playful sense of discovery` — не тот тон.
- `Create one original still frame`, `Wide 16:9 frame` — формат уходит в OUTPUT SETTINGS.
- Запреты `No existing franchise characters, text...` — для видео только позитивные формулировки (S.6).

## STYLE LOCK (дословно, на английском)

```
polished family-friendly 3D animation, appealing rounded proportions, carefully controlled large expressive eyes, tactile but clean materials, believable body structure, consistent limbs, natural contact shadows, strong visual silhouette, premium cinematic 3D lighting, restrained color harmony, original character design
```

Раскладка по блокам-домам видеопромта (S.3):
- STYLE (суффикс): `polished family-friendly 3D animation, appealing rounded proportions, tactile but clean materials, premium cinematic 3D lighting, restrained color harmony, original character design`
- PERFORMANCE: `carefully controlled large expressive eyes`
- PHYSICS: `believable body structure, consistent limbs, natural contact shadows`
- FIRST FRAME: `strong visual silhouette`

## Палитра 60/30/10 (бриф и проверка; в промт — через материал и свет)

| Локация | 60% | 30% | 10% акцент |
|---|---|---|---|
| L1 Затопленная станция (сон) | глубокий бирюзово-тёмный #1E3B44 (вода, тени кафеля) | выцветший кремовый кафель #CFC8B0 | жёлтый плащ #F2B705 + тёплый свет из двери #FFB25A |
| L2 Детская ночью | тёплая умбра #4A3426 (стены, пол в тени) | выцветшее голубое одеяло #6C86A8 | золотая звезда (ночник, кораблик, заколка) #F5C542 |

Цветовая драматургия: холод = потерянность, тепло = дом. Девочка-призрак в детской несёт с собой холодный свет станции — так видно, что она здесь чужая.

## LIGHT LOCK

**L1 станция:** key — длинные ряды ламп дневного света в потолке над платформой, холодные 8500K, сверху; одна дальняя лампа мерцает. Key:fill 4:1. В SH010 дополнительно тёплый 3200K из щели двери справа от неё (самое яркое место кадра); после хлопка двери тёплого света нет.

**L2 детская:** key — ночник-звезда на тумбочке у изголовья кровати (тёплый 3200K, низко, слева от кровати); rim — холодный 8500K свет уличного фонаря через окно с дождём (справа от кровати). Key:fill 4:1. **Девочка-призрак** освещена только холодным 8500K («свет станции остаётся на ней»); тень от ночника отбрасывает только мальчик.

Исключение по причине: SH070 — после пробуждения тёплый ночник ложится и на лицо настоящей девочки (холодного света призрака в кадре больше нет, призрака нет).
