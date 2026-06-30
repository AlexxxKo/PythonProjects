# Нарисуйте квадрат

from lib.funcs import get_float_number
from lib.turtle_funcs import run_turtle, draw_right_polygone


@run_turtle
def main(side: float) -> None:
    draw_right_polygone(4, side)


side = get_float_number('Введите длину стороны квадрата:')

main(side)