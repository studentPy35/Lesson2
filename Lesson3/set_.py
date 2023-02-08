set_1 = set()
set_1.add(2)
set_1.add('apple')
set_1.add(3)
set_1.add('strawberry')
print(set_1)
# создаем второе множество
set_2 = {5, 5, 6, 7, 'apple'}

# находим пересечение множеств
general_set = set_1.intersection(set_2)
print(general_set)

# печатаем расзность множеств
print(set_1.difference(set_2))

# симметрическая разность множеств
print(set_1.symmetric_difference(set_2))

# проверяем является ли подмножеством
print(general_set.issubset(set_1))
