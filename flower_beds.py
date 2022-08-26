from typing import List


def read_input() -> list:
    gardeners = int(input())
    clumbs = []
    for _ in range(gardeners):
        clumbs.append(list(map(int, input().split())))
    return clumbs


def clumb_creator(sorted_clumbs: List[list]) -> None:
    begin, end = sorted_clumbs[0]
    for clumb in sorted_clumbs[1:]:
        if clumb[0] > end:
            print(begin, end)
            begin, end = clumb
        else:
            end = max(end, clumb[1])
    print(begin, end)


if __name__ == '__main__':
    sorted_clumbs = sorted(read_input())
    clumb_creator(sorted_clumbs)
