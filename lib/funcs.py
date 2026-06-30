def get_int_number(question: str, be_negative: bool = False) -> int:
    while True:
        try:
            n = int(input(f'{question} '))
            if not be_negative and n < 0:
                raise ValueError
            break
        except ValueError:
            print(f'Нужно ввести целое {"" if be_negative else "не отрицательное "}число\n')

    return n

def get_float_number(question: str, be_negative: bool = False) -> float:
    while True:
        try:
            n = float(input(f'{question} '))
            if not be_negative and n < 0:
                raise ValueError
            break
        except ValueError:
            print(f'Нужно ввести {"" if be_negative else "не отрицательное "}число\n')

    return n

