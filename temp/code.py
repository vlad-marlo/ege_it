'''
https://inf-ege.sdamgia.ru/test?theme=217
13 номер егэ
'''
commands = [
    lambda x: x + 1,
    lambda x: x * 2 + 1,
]

def solution(num, match: int, exclude: int) -> int:
    counter = 0
    def inner(num: int, match: int, exclude: int):
        nonlocal counter
        if num == exclude or num > match:
            return None
        if num == match:
            counter += 1
        for i in range(2):
            inner(commands[i](num), match, exclude)
    inner(num, match, exclude)
    return counter


print(solution(1, 27, 26))
