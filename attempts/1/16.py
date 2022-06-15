def fib(n: int):
    if n > 2:
        return fib(n - 1) + fib(n - 2)
    return 1

print(fib(6))
