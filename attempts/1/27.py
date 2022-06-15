from typing import List


def read_data(filename: str) -> List[int]:
    with open(filename, 'r') as file:
        return sorted(map(int, file.read().strip().split()))


def solution(data: List[int]):
    idk = lambda x: x % 3
    _sum = data[0:3]
    min_sum = sum(_sum)
    diff = min_sum % 3
    if diff == 0:
        return min_sum
    for i in range(3, len(data)):
        for num in _sum:
            if idk(data[i] + num + min_sum) == 0:
                min_sum = min(min_sum + data[i] - num, min_sum)
                diff = min_sum % 3
    return min_sum



def main():
    filenames = ['27-A.txt', '27-B.txt']
    for file in filenames:
        print(solution(read_data(file)))


if __name__ == '__main__':
    main()
