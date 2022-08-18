def read_input() -> str:
    return input().strip()


def is_correct_bracket_seq(brackets: str) -> bool:
    result = []
    open_breacket = '({['
    close_breacket = ')}]'
    for s in brackets:
        if s in open_breacket:
            result.append(s)
        elif s in close_breacket and result:
            if s == close_breacket[0] and result[-1] == open_breacket[0]:
                result.pop()
            elif s == close_breacket[1] and result[-1] == open_breacket[1]:
                result.pop()
            elif s == close_breacket[2] and result[-1] == open_breacket[2]:
                result.pop()
            else:
                return False
        else:
            return False
    if result:
        return False
    return True


if __name__ == '__main__':
    bracket_seq = read_input()
    print(is_correct_bracket_seq(bracket_seq))
