def read_input() -> str:
    return input()


def combo(numbers, start_nums=0, string=''):
    count = len(numbers)
    if start_nums == count:
        print(string, end=' ')
    else:
        chars = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        num = int(numbers[start_nums])
        for char in chars[num]:
            combo(numbers, start_nums + 1, string + char)


if __name__ == '__main__':
    combo(read_input())
