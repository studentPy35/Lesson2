x = int(input('Введите число х: '))
y = int(input('Введите число y: '))
addition = x + y
print('Сумма:', addition)
multiplication = x * y
print('Произведение:', multiplication)
difference = x - y
print('Разность:', difference)
division = x / y
print('Частное:', division)
modulo = x % y
print('Остаток от деления х на y:', modulo)
integer_division = x // y
print('Целочисленное деление х на y:', integer_division)
print()


text = 'TeachMeSkills'
print(text[::-1])
print(text[1])
print('Печатаем слово чай:', text[:3])
print(text.index('Me'))
print(text.isalpha())
print(text.upper())


print(bool(1))
print(bool([]))
print(bool(None))
print(bool({1, 2, 3}))
print(bool({}))
print(bool(tuple()))


x = 2
print(float(x))
y = 2.123456789
print(round(float(y), 4))
print(2.1 + 2.5)
print(2.5 / 2)
