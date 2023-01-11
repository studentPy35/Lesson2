# создаем и печатаем кортеж из одного элемента
shop_list_1 = ('apple',)
print(shop_list_1)

# создаем кортеж и обращаем к элементам по их индексу, печатаем срезы
shop_list_2 = ('apple', 'pineapple', 'banana', 'blueberry')
print(shop_list_2[0])
print(shop_list_2[-1])
print(shop_list_2[:])
print(shop_list_2[1:3])

# печатаем длину кортежа
print(len(shop_list_2))

# печатаем количество элемента 'apple' в кортеже
print(shop_list_2.count('apple'))

# печатаем индекс элемента 'banana'
print(shop_list_2.index('banana'))