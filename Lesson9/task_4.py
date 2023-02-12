from math import sqrt


def get_length(point1: tuple, point2: tuple) -> float:
    """The function takes 2 points (tuples), returns
    the length of the segment
    """
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def get_common_length(*args: tuple) -> float:
    """The function takes the n numbers of tuples
    (coordinate points), consisting of two int objects,
    and returns the length of the path between these
    coordinates
    """
    length = 0
    for index in range(len(args) - 1):
        length += get_length(args[index], args[index + 1])
    return length


result = get_common_length((1, 1), (1, 2), (2, 3))
print(round(result, 1))
