from typing import Tuple


def read_input() -> Tuple[int, list]:
    lenght_array = int(input())
    numbers = list(map(int, input().strip().split()))
    return lenght_array, numbers


def bubble(lenght_array: int, numbers: list) -> None:
    count = 0
    count_2 = 0
    for i in range(lenght_array - 1):
        for j in range(lenght_array - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                count += 1
        if count:
            print(*numbers)
            count = 0
            count_2 += 1
    if not count_2:
        print(*numbers)


if __name__ == '__main__':
    lenght_array, numbers = read_input()
    bubble(lenght_array, numbers)
