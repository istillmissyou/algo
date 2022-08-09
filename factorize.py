from typing import List

def factorize(number: int) -> List[int]:
    result = []
    divisor = 2
    while divisor ** 2 <= number:
        if number % divisor == 0:
            number //= divisor
            result.append(divisor)
        else:
            divisor += 1

    if number != 1:
        result.append(number)

    return sorted(result)

result = factorize(int(input()))
print(" ".join(map(str, result)))
