# Нарисуйте спираль Архимеда.

import turtle as t
from math import sin, cos, pi

from lib.funcs import get_float_number
from lib.turtle_funcs import run_turtle

@run_turtle
def main(a: float, n: float):
    angle = 0.1

    while angle < 2 * n * pi:
        r = a * angle
        x = a * r * cos(angle)
        y = a * r * sin(angle)

        angle_t = t.towards(x, y)
        t.setheading(angle_t)
        t.goto(x, y)

        angle += .1


a = get_float_number('Введите расстояние между витками спирали:')
n = get_float_number('Введите количество витков спирали (можно не целое):')

main(a, n)