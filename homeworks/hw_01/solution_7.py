"""
https://inf-ege.sdamgia.ru/problem?id=3405
"""


def solution(
    num: int,
    match: int,
    commands: list,
    command: str,
    max_len: int
):
    if len(command) <= max_len or num > match:
        if num == match:
            yield command
        else:
            for i in range(len(commands)):
                solution(
                    commands[i](num),
                    match,
                    commands,
                    command + str(i + 1),
                    max_len,
                )


if __name__ == '__main__':
    commands = [
        lambda x: x + 5,
        lambda x: x * 3,
    ]
    answer = solution(3, 59, commands, '', 5)
    print(answer, list(answer), *answer, sep='\n')
