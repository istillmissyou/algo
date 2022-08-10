from typing import List


def nearest_zero(numbers: List[int]) -> List[int]:
    house_number = len(numbers)
    result = [0] * house_number
    zero_indexes = [i for i, v in enumerate(numbers) if numbers[i] == 0]
    for i in range(zero_indexes[0], house_number):
        if numbers[i] == 0:
            result[i] = 0
        else:
            result[i] = result[i - 1] + 1
    for i in range(zero_indexes[-1], zero_indexes[0], -1):
        if numbers[i] == 0:
            result[i] = 0
        else:
            result[i] = min(result[i], result[i + 1] + 1)
    for i in range(zero_indexes[0] - 1, -1, -1):
        result[i] = result[i + 1] + 1
    return result


def read_input() -> List[int]:
    street_length = int(input())
    house_numbers = list(map(int, input().strip().split()))
    return house_numbers


if __name__ == '__main__':
    numbers = read_input()
    print(" ".join(map(str, nearest_zero(numbers))))
