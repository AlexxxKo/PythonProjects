# Нарисуйте паука с n лапами

import turtle as t

from lib.funcs import get_int_number, get_float_number
from lib.turtle_funcs import run_turtle, draw_line


@run_turtle
def main(n: int, side: float) -> None:
    angle = 360 / n
    for i in range(n):
        draw_line(side, True)
        t.right(angle)
    t.stamp()

n = get_int_number('Введите количество ног у паука:')
side = get_float_number('Введите размер ног паука:')

main(n, side)