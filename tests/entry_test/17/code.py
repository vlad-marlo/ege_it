"""
В файле содержится последовательность из 10 000 целых положительных чисел.
Каждое число не превышает 10 000. Определите и запишите в ответе сначала 
количество пар элементов последовательности, у которых сумма элементов кратна 
60 и хотя бы один элемент из пары делится на 40, затем максимальную из сумм 
элементов таких пар. В данной задаче под парой подразумевается два различных 
элемента последовательности. Порядок элементов в паре не важен.
"""
from typing import List, Tuple




def read_data() -> List[int]:
    with open('17.txt') as file:
        return list(
            map(
                int,
                set(
                    filter(lambda x: x[-1] == '0', file.read().strip().split())
                )
            )
        )


def check(first: int, second: int) -> bool:
    return ((first + second) % 60 == 0) and (first % 40 == 0 or second % 40 == 0) 


def solution(data: List[int]) -> Tuple[int, int]:
    max_summ, count = 0, 0
    first, second = None, None
    for first in range(len(data) - 1):
        for second in range(first, len(data)):
            if check(data[first], data[second]):
                max_summ = max(data[first] + data[second], max_summ)
                count += 1
    return count, max_summ


if __name__ == '__main__':
    print(*solution(read_data()), sep=' count <== | ==> max_summ ')
