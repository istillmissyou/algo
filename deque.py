class CustomOverflowError(Exception):
    def __init__(self) -> None:
        self.message = 'Deque is overflow'
        super().__init__(self.message)


class EmptyError(Exception):
    def __init__(self) -> None:
        self.message = 'Deque is empty'
        super().__init__(self.message)


class Deque:
    def __init__(self, max_size: int) -> None:
        self.__list = [None] * max_size
        self.__max_n: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_overflowed(self) -> bool:
        return self.__size == self.__max_n

    def push_back(self, value: int) -> None:
        if self.is_overflowed():
            raise CustomOverflowError()
        self.__list[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1

    def push_front(self, value: int) -> None:
        if self.is_overflowed():
            raise CustomOverflowError()
        head_front = self.__head - 1
        self.__list[head_front] = value
        self.__head = (head_front) % self.__max_n
        self.__size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise EmptyError()
        value = self.__list[self.__head]
        self.__head = (self.__head + 1) % self.__max_n
        self.__size -= 1
        return value

    def pop_back(self) -> int:
        if self.is_empty():
            raise EmptyError()
        tail_back = self.__tail - 1
        value = self.__list[tail_back]
        self.__tail = (tail_back) % self.__max_n
        self.__size -= 1
        return value


if __name__ == '__main__':
    number_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size=max_size)

    for _ in range(number_commands):
        command = input().split()
        if len(command) > 1:
            try:
                getattr(deque, command[0])(value=command[1])
            except CustomOverflowError:
                print('error')
            except EmptyError:
                print('error')
        else:
            try:
                print(getattr(deque, command[0])())
            except CustomOverflowError:
                print('error')
            except EmptyError:
                print('error')
