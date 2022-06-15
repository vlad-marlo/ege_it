from typing import Tuple


def algo(num: int) -> Tuple:
    a, b = 0, 1
    while num > 0:
        a += 1
        b *= num % 1000
        num //= 1000
    return a, b


num = 1
while list(algo(num)) != [2, 11]:
    num += 1
print(algo(num), num)


