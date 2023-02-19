from collections import defaultdict


def get_common_dict(first_dct: dict, second_dct: dict) -> dict:
    """The function takes 2 dictionaries and returns a dictionary,
    where the keys are keys from both dictionaries, values - list
    of values in dictionaries (1st position for the 1st
    dictionary, second for the 2nd), if the key is not in
    the dictionary, returns None
    """
    key_list = set(list(first_dct.keys()) + list(second_dct.keys()))
    result = defaultdict(list)
    for item in key_list:
        result[item].append(first_dct.get(item))
        result[item].append(second_dct.get(item))

    return dict(result)


print(get_common_dict({'a': 1, 'b': 2, 'c': 3, 'x': 10},
                      {'c': 3, 'd': 4, 'e': 5}))
