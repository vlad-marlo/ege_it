'''
https://inf-ege.sdamgia.ru/test?theme=217
13 номер егэ
'''
commands = [
    lambda x: x + 1,
    lambda x: x * 2 + 1,
]


def solution(num: int, match: int, exclude: int):
    if num == exclude or num > match:
        return 0
    if num == match:
        return 1
    return sum([solution(commands[i](num), match, exclude) for i in range(len(commands))])


print(solution(1, 27, 26))
