text = input('Введите произвольную строку: ')
even_numbers = text[:]
uneven_numbers = text[:]               # TODO можно попробовать решить через списки, которые потом переведем в строки


for i in text:
    if i.isdigit():                    # проверяем является ли элемент числом
        if int(i) % 2 == 0:            # проверяем является ли число четным
            uneven_numbers = uneven_numbers.replace(i, '')
        else:
            even_numbers = even_numbers.replace(i, '')
    else:                              # если элелемент не является числом, удаляем его
        even_numbers = even_numbers.replace(i, '')
        uneven_numbers = uneven_numbers.replace(i, '')

print(f'Введенная строка "{text.strip()}"', end='  ')
print(even_numbers, uneven_numbers, sep='     ', end='\n!!!')

