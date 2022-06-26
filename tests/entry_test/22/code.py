def algo(x):
    l = x - 30
    m = x + 60
    while l != m:
        if l > m:
            l -= m
        else:
            m -= l
    return m


def solution() -> int:
    num = 101
    while algo(num) != 30:
        num += 1
    return num


print(solution())
