from typing import List, Tuple

NUMBER_OF_LINES = 4
PLAYERS = 2


def sleight_of_hand(clicks: int, symbols: List[str]) -> int:
    del_symbols = set()
    symbol_keys = {x: 0 for x in set(symbols) if x != '.'}
    players_clicks = clicks * PLAYERS
    for symbol in symbols:
        if symbol != '.' and symbol not in del_symbols:
            symbol_keys[symbol] += 1
            if symbol_keys[symbol] > players_clicks:
                del_symbols.add(symbol)
                del symbol_keys[symbol]
    return len(symbol_keys)


def read_input() -> Tuple[List[str], int]:
    clicks = int(input())
    symbols = ''.join((input().strip() for _ in range(NUMBER_OF_LINES)))
    return clicks, list(symbols)


if __name__ == '__main__':
    clicks, symbols = read_input()
    print(sleight_of_hand(clicks, symbols))
