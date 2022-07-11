"""
https://inf-ege.sdamgia.ru/test?id=11207318
2 решения задачи https://inf-ege.sdamgia.ru/problem?id=5305
"""

commands = [
    lambda x: x - 1,
    lambda x: x * 5,
]


class Solution:
    """
    Да, я немного увлекся. Знаю что можно и проще(
    Ниже есть еще вариант, но там я, вроде, тоже начудил.
    """

    def __init__(self, num: int, match: int) -> None:
        self.__base_num = num
        self.__match = match
        self.__codes = []
        self.__min_depth = 5

    def __get_min_depth(self, num: int, depth: int):
        if num == self.__match:
            return depth
        if depth >= 5:
            return depth
        self.__min_depth = min(
            [
                self.__get_min_depth(commands[i](num), depth + 1) for i in range(len(commands))
            ]
        )
        return 5

    def __gen_codes(self, code: str='', depth: int=0):
        if depth == 0:
            self.__get_min_depth(self.__base_num, 0)
        if depth == self.__min_depth:
            return self.__codes.append(code)
        for i in range(len(commands)):
            self.__gen_codes(code + str(i), depth + 1)

    def __run_codes(self):
        for code in self.__codes:
            num = self.__base_num
            for i in code:
                num = commands[int(i)](num)
            if num == self.__match:
                code = code.replace('1', '2')
                code = code.replace('0', '1')
                return code
        return '-1'

    def __str__(self) -> str:
        self.__gen_codes()
        return self.__run_codes()


def base_solution(num: int, match: int, command=None, answer=[]):
    command = '' if command is None else command
    if len(command) > 5 and num != match:
        return 0
    if num == match:
        command = command.replace('1', '2')
        command = command.replace('0', '1')
        print(command)
        return answer.append(command)
    for i in range(len(commands)):
        base_solution(commands[i](num), match, command + str(i))


if __name__ == '__main__':
    print(Solution(1, 99))
    base_solution(1, 99)
