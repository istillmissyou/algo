OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def read_input() -> list:
    return input().strip().split()


def calculator(expression: list) -> int:
    stack = Stack()
    for symbols in expression:
        try:
            if isinstance(int(symbols), int):
                stack.push(symbols)
        except ValueError:
            num_1, num_2 = int(stack.pop()), int(stack.pop())
            stack.push(OPERATORS[symbols](num_2, num_1))
    return stack.pop()


if __name__ == '__main__':
    expression = read_input()
    print(calculator(expression))
