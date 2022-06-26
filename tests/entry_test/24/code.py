def read_data() -> str:
    with open('24_demo.txt', 'r') as file:
        return file.read().strip()


def solution(string):
    streek = 0
    temp_streek = 0
    index = 0
    while index < len(string):
        print(string[index])
        if string[index] == 'Y':
            temp_streek += 1
        else:
            streek = max(streek, temp_streek)
            temp_streek = 0
        index += 1
    return streek


print(solution(read_data()))

