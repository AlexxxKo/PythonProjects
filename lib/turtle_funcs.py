import turtle as t

def draw_line(side: float | int, is_stamp: bool = False) -> None:
    t.forward(side)
    if is_stamp:
        t.stamp()
    t.backward(side)


def draw_right_polygone(n: int, side: float | int) -> None:
    angle = 180 - (n - 2) * 180 / n
    for _ in range(n):
        t.forward(side)
        t.left(angle)


def run_turtle(func):
    def wrapper(*args, shape: str = None, **kwargs):
        t.shape('turtle' if shape is None else shape)
        t.speed(0)
        func(*args, **kwargs)
        t.hideturtle()
        t.done()
    return wrapper