from math import sqrt


def get_length(point1: tuple, point2: tuple) -> int:
    """Функция принимает 2 точки(кортежа), возвращает  длину отрезка"""
    result = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    return result


def get_common_length(*args: tuple) -> int:
    """Функция принимает n-ое количество кортежей (точек координат),
     состоящих из двух объектов типа int, и возвращает длину пути
     между этими координатами
    """
    length = 0
    for index in range(len(args) - 1):
        length += get_length(args[index], args[index + 1])
    return length


result = get_common_length((1, 1), (1, 2), (2, 3))
print(round(result, 1))
