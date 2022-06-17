'''
https://inf-ege.sdamgia.ru/test?theme=217
13 номер егэ
'''
commands = [
    lambda x: x + 1,
    lambda x: x * 2 + 1,
]
counter = 0

def solution(num: int, match: int, exclude: int):
    global counter
    if num == exclude or num > match:
        return None
    if num == match:
        counter += 1
    for i in range(2):
        solution(commands[i](num), match, exclude)


solution(1, 27, 26)
print(counter)
