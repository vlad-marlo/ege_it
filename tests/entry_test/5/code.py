def transform(num: str) -> int:
    even = int(num[1]) * int(num[3])
    not_even = int(num[0]) * int(num[2])
    return int(''.join(map(str, sorted([even, not_even]))))


def main() -> None:
    num = 1000
    while transform(str(num)) != 124 or num > 9999:
        num += 1
    print(num)



if __name__ == '__main__':
    main()
