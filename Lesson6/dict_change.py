def dict_change(dct: dict) -> dict:
    new_dict = {}
    for key, value in dct.items():
        new_dict.update({value: key})
    return new_dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict_change(my_dict))
