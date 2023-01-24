from math import factorial

def factorial_1(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial_1(n - 1)

def factorial_2(n: int) -> int:
    return factorial(n)


print(factorial_1(5))
print(factorial_2(5))
