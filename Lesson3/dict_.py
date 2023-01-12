# создаем словарь
my_dict = {'hi': 1, 'privet': 2, 'namaste': 3}
# печатаем значение по ключу 'privet'
print(my_dict['privet'])

# добавляем элемент словаря
my_dict['alloha'] = 4

# объединяем два словаря и печатаем результат
my_dict.update({'hello': 5})
print(my_dict)

# выводим значение по ключу 'hi', в случае его отсутствия вернет None
print(my_dict.get('hi'))
print(my_dict.get('zdorova'))

# печатаем список ключей словаря
print(list(my_dict.keys()))

# создаем новый словарь из списка кортежей
new_dict = dict([('hola', 6), ('bonjur', 7)])
print(new_dict)
# печатаем значения словаря в виде итеррируемого объекта словаря
print(new_dict.values())
