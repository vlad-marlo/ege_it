transform = lambda num: int(''.join(map(str, sorted([sum([int(num[i]), int(num[i + 1])]) for i in range(len(num) - 1)], reverse=True))))
num = 100
while transform(str(num)) != 1412:
    num += 1
print(num)
