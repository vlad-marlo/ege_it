def to_system(num: int, base: int) -> str:
    answer = ''
    while num:
        answer += str(num % base)
        num //= base
    return answer[::-1]



for i in range(4, 8):
    print(to_system(int('65', 8), i), i)

