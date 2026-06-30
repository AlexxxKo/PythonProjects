# Нарисуйте букву S

import turtle as t

from lib.funcs import get_float_number
from lib.turtle_funcs import run_turtle

@run_turtle
def main(side: float) -> None:
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)

side = get_float_number('Введите ширину буквы:', True)

main(side)