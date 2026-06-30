# Нарисуйте n вложенных квадратов с шагом step.

import turtle as t

from lib.funcs import get_float_number, get_int_number
from lib.turtle_funcs import run_turtle, draw_right_polygone

@run_turtle
def main(n, step):
    side = 10
    for i in range(n):
        draw_right_polygone(4, side)
        t.penup()
        t.backward(step)
        t.right(90)
        t.forward(step)
        t.left(90)
        t.pendown()
        side += 2 * step

n = get_int_number('Введите количество квадратов:')
step = get_float_number('Введите расстояние между квадратами:')

main(n, step)