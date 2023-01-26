from beartype import beartype

@beartype
def get_digit(text: str) -> str:
    '''Функция для распознавания чисел: положительных или отрицательных, целых или дробных.'''
    if text.replace('.', '', 1).replace('-', '', 1).isdigit() and '-' not in text[1:]:
        if '.' not in text:
            if int(text) > 0:
                return f'Вы ввели целое положительное число: {text}'
            else:
                return f'Вы ввели целое отрицательное число: {text}'
        else:
            if float(text) > 0:
                return f'Вы ввели положительное дробное число: {text}'
            else:
                return f'Вы ввели отрицательное дробное число: {text}'
    else:
        return f'Вы ввели не корректное число: {text}'

digit = input('Введите строку: ')
print(get_digit(digit))






