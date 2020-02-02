"""
Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость — безграничная,
ограниченная, или замкнутая (в пределе — бесконечная плоскость).
Каждая клетка на этой поверхности может находиться в двух состояниях: быть «живой» (заполненной)
или быть «мёртвой» (пустой). Клетка имеет восемь соседей   , окружающих её.
Распределение живых клеток в начале игры называется первым поколением.
Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:
    в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
    если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить;
    в противном случае, если соседей меньше двух или больше трёх, клетка умирает («от одиночества»
    или «от перенаселённости»)
Игра прекращается, если
    на поле не останется ни одной «живой» клетки
    конфигурация на очередном шаге в точности (без сдвигов и поворотов) повторит себя же на
    одном из более ранних шагов (складывается периодическая конфигурация)
    при очередном шаге ни одна из клеток не меняет своего состояния (складывается стабильная конфигурация;
    предыдущее правило, вырожденное до одного шага назад)
Игрок не принимает прямого участия в игре, а лишь расставляет или генерирует начальную конфигурацию «живых» клеток,
которые затем взаимодействуют согласно правилам уже без его участия (он является наблюдателем).
"""

from random import choice

MAX_SIZE = 10
DEAD = ' '
LIVE = 'x'


def neighbor_xy(x, y):
    for dx, dy in (
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1)
    ):
        yield x + dx, y + dy


def show_field(field):
    for y in range(MAX_SIZE):
        print(''.join(field[y]))


def get_empty_field():
    return [
        [DEAD for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
    ]


def is_live(field, neighbor_x, neighbor_y):
    return 0 <= neighbor_x < MAX_SIZE \
           and 0 <= neighbor_y < MAX_SIZE \
           and field[neighbor_y][neighbor_x] == LIVE


field = [
    [choice([DEAD, LIVE]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]

while True:
    input('press any key for next step: ')
    show_field(field)
    buffer = get_empty_field()
    for y in range(MAX_SIZE):
        for x in range(MAX_SIZE):
            c = field[y][x]
            neighbors = 0
            for neighbor_x, neighbor_y in neighbor_xy(x, y):
                neighbors += 1 if is_live(field, neighbor_x, neighbor_y) else 0
            if c == DEAD:
                buffer[y][x] = LIVE if neighbors == 3 else DEAD
            else:
                buffer[y][x] = LIVE if neighbors in (2, 3) else DEAD

    if field == buffer:
        print('stasis')
        break
    field = buffer
