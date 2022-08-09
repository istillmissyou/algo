from typing import List, Tuple

NUMBER_OF_LINES = 4
PLAYERS = 2


def sleight_of_hand(clicks: int, char_list: List[str]) -> int:
    del_char = set()
    char_dict = {x: 0 for x in set(char_list) if x != '.'}
    for s in char_list:
        if s != '.' and s not in del_char:
            char_dict[s] += 1
            if char_dict[s] > clicks * PLAYERS:
                del_char.add(s)
                del char_dict[s]
    return len(char_dict)

def read_input() -> Tuple[List[str], int]:
    clicks = int(input())
    char_list = ''.join((input().strip() for _ in range(NUMBER_OF_LINES)))
    return clicks, list(char_list)

clicks, char_list = read_input()
print(sleight_of_hand(clicks, char_list))
