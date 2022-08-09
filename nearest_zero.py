from typing import List


def nearest_zero(number_list: List[int]) -> List[int]:
    house_number = len(number_list)
    result = [0] * house_number
    zero_indices = [i for i in range(house_number) if number_list[i] == 0]
    for i in range(zero_indices[0], house_number):
        if number_list[i] == 0:
            result[i] = 0
        else:
            result[i] = result[i - 1] + 1
    for i in range(zero_indices[-1], zero_indices[0], -1):
        if number_list[i] == 0:
            result[i] = 0
        else:
            result[i] = min(result[i], result[i + 1] + 1)
    for i in range(zero_indices[0] - 1, -1, -1):
        result[i] = result[i + 1] + 1
    return result

def read_input() -> List[int]:
    n = int(input())
    return list(map(int, input().strip().split()))

number_list = read_input()
print(" ".join(map(str, nearest_zero(number_list))))
