"""
https://inf-ege.sdamgia.ru/problem?id=27375
"""

def to_system(num, base) -> str:
    answer = str(num % base)
    while num:
        answer += str(num % base)
        num //= base
    return answer[::-1]


def solution(num: int) -> int:
    return int(to_system(num, 3), 3)


if __name__ == '__main__':
    num = 1
    while len(str(solution(num))) != 3:
        num += 1
    print(num, solution(num))
