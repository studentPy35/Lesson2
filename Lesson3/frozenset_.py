# создаем frozenset и печатаем их
myset1 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])
myset2 = frozenset('aabcccddee')

print(myset1)
print(myset2)

# объединяем два frozenset
print(myset2.union(myset1))

# находим пересечение множеств
print(myset2.intersection(myset1))
