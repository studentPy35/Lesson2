from time import perf_counter
from beartype import beartype


def timer(iters=1):
    '''Декоратор для определения времени выполнения функции, который принимает 1 аргумент - количество измерений'''
    def decorator(func):
        '''Сам декоратор'''
        def wrapper(*args, **kwargs):
            '''Для функции, которая примимает переменное количество позиционных и именнованных аргументов'''
            total = 0
            for i in range(iters):
                start_time = perf_counter()
                result = func(*args, **kwargs)
                end_time = perf_counter()
                total += end_time - start_time
            print(f'Время выполнения функции {func.__name__}: {round(total / iters, 5)} сек.')
            print(f'Результат выполнения функции:')
            return result
        return wrapper
    return decorator


@timer(5)
@beartype
def map_func(lst: list) -> list:
    '''Функция принимает список чисел, возвращает список строк'''
    return list(map(lambda num: str(num), lst))

lst = [1, 2, 3, 4, 5, 6, 7]

print(map_func(lst))


@timer()
@beartype
def factorial_1(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial_1(n - 1)

print(factorial_1(5))


