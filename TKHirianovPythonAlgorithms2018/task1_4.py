# Нарисуйте окружность, не используя circle()

from math import pi

from lib.funcs import get_float_number
from lib.turtle_funcs import run_turtle, draw_right_polygone


@run_turtle
def main(r: float) -> None:
    l = 2 * pi * r
    n = 100
    side = l / n

    draw_right_polygone(n, side)


r = get_float_number('Введите радиус окружности:')

main(r)
