from typing import List, Union


def get_count_of_dels(num: int) -> int:
    counter = 0
    for del_ in range(1, num):
        if num % del_ == 0:
            counter += 1
    return counter


def solution():
    primes: List[Union[int, None]] = [i for i in range(2, 569230)]
    for i in range(len(primes)):
        if primes[i] is not None:
            for x in range(i, len(primes), i + 2):
                primes[x] = None
    max_dels, min_num = 0, 0
    for num in range(568023, 569230):
        if num in primes:
            continue
        count = get_count_of_dels(num)
        if count > max_dels:
            max_dels, min_num = count, num
    print(max_dels, min_num)


solution()

