from typing import Tuple


def read_input() -> Tuple[str]:
    return input(), input()


def is_subsequence(string_1, string_2) -> bool:
    start = -1
    for i in string_1:
        start = string_2.find(i, start + 1)
        if start == -1:
            return False
    return True


if __name__ == '__main__':
    print(is_subsequence(*read_input()))
