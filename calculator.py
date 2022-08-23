OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


class EmptyError(Exception):
    def __init__(self) -> None:
        self.message = 'Stack is empty'
        super().__init__(self.message)


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) == 0:
            raise EmptyError()
        return self.__items.pop()


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
        except EmptyError:
            print('Стек пуст!')
    return stack.pop()


if __name__ == '__main__':
    expression = read_input()
    print(calculator(expression))
