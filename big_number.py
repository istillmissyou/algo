from typing import Callable, List, Tuple


def read_input() -> Tuple[int, str]:
    amount_number = int(input())
    numbers = input().strip().split()
    return amount_number, numbers


def comparator(string_1: str, string_2: str) -> bool:
    return string_1 + string_2 < string_2 + string_1


def big_number(numbers: List[str], func: Callable) -> str:
    for i in range(1, len(numbers)):
        item_to_insert = numbers[i]
        j = i
        while j > 0 and func(numbers[j - 1], item_to_insert):
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = item_to_insert
    return ''.join(numbers)


if __name__ == '__main__':
    amount_number, numbers = read_input()
    print(big_number(numbers, comparator))
