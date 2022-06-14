from typing import List, Optional, Union


check = lambda x, y: bool(x * y % 49 != 0 and ((x % 7 == 0) or (y % 7 == 0)))


def read_data(filename: Optional[str]=None) -> List[int]:
    with open('27986_A.txt' if filename is None else filename, 'r') as file:
        data = []
        readline = int(file.readline())
        while readline != 0:
            data.append(readline)
            readline = int(file.readline())
        return list(set(data))


def solution(data: List[int]) -> int:
    max_con = 1
    for first in range(len(data) - 1):
        for second in range(first, len(data)):
            if check(data[first], data[second]):
                max_con = max(max_con, data[first] + data[second])
    return max_con



if __name__ == '__main__':
    print(solution(read_data()))
    print(solution(read_data('27986_B.txt')))
