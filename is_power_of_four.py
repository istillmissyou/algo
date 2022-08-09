from math import log


def is_power_of_four(number: int) -> bool:
    return log(number, 4) % 1 == 0.0

print(is_power_of_four(int(input())))
