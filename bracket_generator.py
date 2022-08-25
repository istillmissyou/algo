def read_input() -> int:
    return int(input())


def generator_bracket(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            generator_bracket(count, s + '(', left + 1, right)
        if right < left:
            generator_bracket(count, s + ')', left, right + 1)


if __name__ == '__main__':
    count = read_input()
    generator_bracket(count)
