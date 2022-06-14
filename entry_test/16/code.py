def f(n):
    if n > 2:
        return f(n - 1) + g(n - 2)
    return n + 1


def g(n):
    if n > 2:
        return f(n - 2) + g(n - 1)
    return n


print(g(7))
