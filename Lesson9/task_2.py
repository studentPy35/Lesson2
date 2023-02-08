from collections import defaultdict


def get_common_dict(first_dct: dict, second_dct: dict) -> dict:
    """Функция принимает 2 словаря и возвращает словарь, где ключи -
    ключи из обоих словарей, значения - список значений ключей в
    словарях (1-я позиция для 1-ого словаря, вторая для 2-ого),
    если ключа нет в словаре - возвращает значение None
    """
    dict_list = [first_dct, second_dct]
    key_list = []
    [key_list.append(key) for item in dict_list
     for key in item.keys() if key not in key_list]
    result = defaultdict(list)
    for item in dict_list:
        for key in key_list:
            result[key].append(item.get(key))

    return dict(result)


print(get_common_dict({'a': 1, 'b': 2, 'c': 3, 'x': 10},
                      {'c': 3, 'd': 4, 'e': 5}))
