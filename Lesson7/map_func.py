from beartype import beartype


@beartype
def map_func(lst: list) -> list:
    '''Функция принимает список чисел, возвращает список строк'''
    return list(map(lambda num: str(num), lst))

lst = [1, 2, 3, 4, 5, 6, 7]

print(map_func(lst))