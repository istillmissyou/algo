OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


def read_input() -> list:
    return input().strip().split()


def calculator(expression: list) -> int:
    stack = []
    for symbols in expression:
        try:
            if isinstance(int(symbols), int):
                stack.append(symbols)
        except ValueError:
            num_1, num_2 = int(stack.pop()), int(stack.pop())
            stack.append(OPERATORS[symbols](num_2, num_1))
    return stack.pop()


if __name__ == '__main__':
    expression = read_input()
    print(calculator(expression))
