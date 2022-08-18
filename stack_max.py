class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else print('error')

    def get_max(self):
        print(max(self.items, default=None))


stack = StackMax()

for _ in range(int(input())):
    list_command = input().split()
    if list_command[0] == 'push':
        stack.push(int(list_command[1]))
    elif list_command[0] == 'pop':
        stack.pop()
    elif list_command[0] == 'get_max':
        stack.get_max()
