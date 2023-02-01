'''3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в
качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.'''
from beartype import beartype
import json

@beartype
def create_dictionary(items: int) -> dict:
    '''Возвращает словарь, где ключ: 6-значное число (id), значение: кортеж из 2-х элементов - имя(str), возраст(int)'''

    name_age = [(input('Введите имя: '), int(input('Введите возраст: '))) for _ in range(items)]
    id_list = [int(str((id(tpl)))[-6:]) for tpl in name_age]
    return dict(zip(id_list, name_age))

item_amount = int(input('Введите количество элементов словаря: '))

with open('create_dict.json', 'w', encoding='utf-8') as output_file:
    json.dump(create_dictionary(item_amount), output_file, indent='  ')




