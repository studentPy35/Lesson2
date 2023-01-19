import random

print('Привет! Это числовая угадайка! Мы загадали целое число от 0 до 100.\nПопробуй его угадать)' )
hidden_number = random.randint(0, 100)
your_number = int(input('Введи целое число от 0 до 100 включительно: '))

while hidden_number != your_number:
    if your_number > hidden_number:
        print('Ваше число больше загаданного. Попробуйте еще раз!')
    elif your_number < hidden_number:
        print('Ваше число меньше загаданного. Попробуйте еще раз!')
    your_number = int(input('Загадайте целое число от 0 до 100 включительно: '))
else:
    print('Поздравляю! Вы угадали!!!')
