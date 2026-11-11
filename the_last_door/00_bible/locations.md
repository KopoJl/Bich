# Локации — Location Lock и промты карт (A.15)

## L1. Затопленная станция метро (сон Уиллы)

Логика места (A.10 п. 2): старая маленькая станция одного пути. Платформа залита стоячей водой на 0.15 м. Вдоль задней стены кафель, в одной точке стены — дверь детской (сон вставил домашнюю дверь в стену станции). Справа от двери платформа уходит в узкий выложенный кафелем переход, в конце перехода — та же дверь второй раз (SH030).

**LOCATION LOCK L1:** small old single-track metro platform flooded with still dark water 15 cm deep; cream-white glazed wall tiles with dark grout, some tiles chipped; long rows of cold fluorescent tubes along the ceiling, one far tube flickering; a pale-blue painted wooden bedroom door with a round brass knob set into the tiled back wall; to its right a narrow tiled passage leads away, ending in the same pale-blue door.

**Карта места (зоны, вид с платформы на заднюю стену):**
- слева: передний — край платформы, вода переливается на пути; средний — кафельная стена, скамья по колено в воде; задний — тёмный тоннель.
- центр: передний — гладь воды с отражением ламп; средний — дверь в стене (2.0 м × 0.8 м); задний — стена.
- справа: средний — проём перехода шириной 1.6 м; задний — уходящий вглубь переход, в конце дверь.

**Промт карты L1 (картинка):**
```
Location sheet, 16:9. Style: polished family-friendly 3D animation, tactile but clean materials, premium cinematic 3D lighting, restrained color harmony. An empty view of the set: camera at 1.1 m, level, 35 mm lens, 54° horizontal field of view, no lens distortion.
LEFT: foreground the platform edge with water spilling over onto the tracks; midground cream-white glazed wall tiles with dark grout and a wooden bench standing knee-deep in water; background a dark tunnel mouth.
CENTER: foreground still dark water 15 cm deep reflecting the ceiling lights; midground a pale-blue painted wooden bedroom door 2.0 m tall with a round brass knob set into the tiled wall, closed.
RIGHT: midground a 1.6 m wide opening into a narrow tiled passage; background the passage recedes, ending in an identical pale-blue door.
Light: long rows of cold fluorescent tubes along the ceiling light the platform from above, one far tube flickers; deep shadows in the tunnel and under the bench; the water is dark teal with sharp reflections of the tubes.
Materials: wet glazed tiles, chipped enamel, painted wood with worn edges, brass, still water with tiny ripples from drips.
Space for a small girl to wade along the wall.
No people, no silhouettes, no faces, no human figures, no human-shaped reflections or shadows, no mannequins, no statues of people, no posters with people. No text, no labels, no watermark.
```

## L2. Детская ночью (явь)

Логика места: комната 4.2 × 3.6 м. Дверь (та же бледно-голубая) в стене напротив окна, левее центра. Кровать Уиллы вдоль левой стены изголовьем к окну; тумбочка с ночником-звездой у изголовья. Окно справа, по стеклу дождь. Пол дощатый, на полу у кровати и на одеяле — десятки бумажных корабликов (их делал Пип много вечеров). Мокрое полотенце на лбу спящей Уиллы, миска с водой на тумбочке — она больна, но это не больница.

**LOCATION LOCK L2:** small children's bedroom at night, 4.2 by 3.6 m, warm wooden floorboards, faded wallpaper with tiny stars; a single bed along the left wall with a faded blue quilt; a bedside table with a star-shaped nightlight and a bowl of water; a rain-streaked window on the right; the pale-blue wooden door with a round brass knob across from the window; dozens of white paper boats scattered on the floor by the bed and on the quilt.

**Промт карты L2 (картинка):**
```
Location sheet, 16:9. Style: polished family-friendly 3D animation, tactile but clean materials, premium cinematic 3D lighting, restrained color harmony. An empty view of the set from the corner by the window: camera at 1.0 m, tilted 5° down, 35 mm lens, 54° horizontal field of view, no lens distortion.
LEFT: foreground the foot of a single bed with a faded blue quilt; midground the bed along the left wall, a pillow at the far end; background a bedside table with a glowing star-shaped nightlight and a small bowl of water.
CENTER: foreground warm wooden floorboards with dozens of small white paper boats; midground more paper boats on the quilt edge; background the pale-blue wooden door with a round brass knob, closed.
RIGHT: midground faded wallpaper with tiny printed stars; foreground edge of a rain-streaked window frame.
Light: the star nightlight is the warm key, a small warm pool around the bed head and the boats; cold streetlight through the rainy window lays a blue rim on the floorboards; the corners fall into deep warm-brown shadow.
Materials: soft worn flannel, folded notebook paper, painted wood, glass with running rain drops.
Space for a small boy to sit on the floor beside the bed.
No people, no silhouettes, no faces, no human figures, no human-shaped reflections or shadows, no mannequins, no statues of people, no posters with people. No text, no labels, no watermark.
```

Проверка: направление света на картах совпадает с Light Lock (ночник слева у изголовья, холод из окна справа; на станции лампы сверху).

## Статус карт локаций (GPT image 2.6 sunburst, 16:9)
- `cards/loc_station_v1.png` — кандидат. Заметка: фактура грязи и ржавчины чуть реалистичнее персонажей; яркая полоса отражений в переходе. Buzzy: https://res-prod.buzzy.now/file-service/5318c9f6-a6a2-4a14-b356-5ab40298fb83.png
- `cards/loc_bedroom_v1.png` — отклонена: кораблики ровной сеткой по всему полу (признак «слопа»).
- `cards/loc_bedroom_v1e.png` — правка: куча корабликов у кровати, несколько на одеяле, проход от двери свободен. Кандидат. Buzzy: https://res-prod.buzzy.now/file-service/c55e8c1d-6111-4b02-9daf-b2df85968034.png
