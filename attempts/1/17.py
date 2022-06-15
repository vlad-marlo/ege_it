from typing import List, Tuple


def read_data() -> List[int]:
    with open('17.txt', 'r') as file:
        return list(map(int, file.read().strip().split()))


def solution(data: List[int]) -> Tuple[int, int]:
    print(max(data))
    _max, _count = 0, 0
    for first in range(len(data) - 1):
        for second in range(first, len(data)):
            if (data[first] + data[second]) % 9 == 0 and data[first] != data[second]:
                _count += 1
                _max = max([data[second] + data[first], _max])
    return _count, _max


print(solution(read_data()))
