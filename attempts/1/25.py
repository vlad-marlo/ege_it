for num in range(185311, 185330):
    dels = []
    count = 0
    for del_ in range(2, int(num ** 0.5) + 1):
        if num % del_ == 0:
            count += 2
            if count > 2:
                break
            dels.append([1, del_, num // del_, num])

    if count == 2:
        print(dels)
