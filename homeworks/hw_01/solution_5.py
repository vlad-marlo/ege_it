"""
https://inf-ege.sdamgia.ru/problem?id=27005
"""

def algo(num: int) -> int:
    nums = [s for s in str(num)]
    num_max = int(''.join(sorted(nums, key=int, reverse=True))[:2])
    num_min = int((nums.pop(nums.index(min(filter(lambda x: x != '0', nums)))) + ''.join(sorted(nums, key=int)))[:2])
    return num_max - num_min


if __name__ == '__main__':
    print(algo(238))
    num = 100
    while algo(num) != 70:
        num += 1
    print(num, algo(num))
