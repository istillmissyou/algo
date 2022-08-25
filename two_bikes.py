from typing import Tuple


def read_input() -> Tuple[int, list, int]:
    days = int(input())
    money_day = list(map(int, input().strip().split()))
    price = int(input())
    return days, money_day, price


def two_bikes(money_day: list, price: int, left: int, right: int):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if money_day[mid] >= price and (money_day[mid - 1] < price or mid == 0):
        return mid + 1
    elif price <= money_day[mid]:
        return two_bikes(money_day, price, left, mid)
    else:
        return two_bikes(money_day, price, mid + 1, right)


if __name__ == '__main__':
    days, money_day, price = read_input()
    print(two_bikes(money_day, price, left=0, right=days), end=' ')
    print(two_bikes(money_day, price * 2, left=0, right=days))
