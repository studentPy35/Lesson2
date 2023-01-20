from collections import Counter

def count_of_numbers_1(numbers: list) -> dict:
    return Counter(numbers)


def count_of_numbers_2(numbers: list) -> dict:
    final_dict = {}
    for i in numbers:
        final_dict[i] = final_dict.get(i, 0) + 1
    return final_dict


numbers = [1, 2, 1, 2, 2, 2]
print(count_of_numbers_1(numbers))
print(count_of_numbers_2(numbers))
