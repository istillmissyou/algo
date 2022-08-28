from typing import Tuple


def read_input() -> Tuple[int, list]:
    number_items = int(input())
    colors = list(map(int, input().strip().split()))
    return number_items, colors


def sort_wardrobe(array: list) -> None:
    less = []
    equal = []
    greater = []
    for x in array:
        if x == 0:
            less.append(x)
        elif x == 1:
            equal.append(x)
        else:
            greater.append(x)
    print(*(less + equal + greater))


if __name__ == '__main__':
    number_items, colors = read_input()
    sort_wardrobe(array=colors)
