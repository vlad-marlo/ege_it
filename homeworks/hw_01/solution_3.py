"""
https://inf-ege.sdamgia.ru/problem?id=5869
"""

commands = [
    lambda x: x ** 2,
    lambda x: x + 1
]

answer = []


def base_solution(num: int, match: int, command=None):
    global answer
    command = '' if command is None else command
    if len(command) > 4 and num != match: # 4 можно вынести в доп аргумент
        return 0
    if num == match:
        command = command.replace('1', '2')
        command = command.replace('0', '1')
        answer.append(command)
        return command
    for i in range(len(commands)):
        base_solution(commands[i](num), match, command + str(i))


if __name__ == '__main__':
    base_solution(1, 17)
    print(min(answer, key=len))
