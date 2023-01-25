from beartype import beartype


@beartype
def even_numbers(num: int):
    '''Функция принимает целое число и печатает информацию: четное или нечетное число.'''
    result = lambda num: num % 2
    if result(num) == 0:
        print('Число четное')
    else:
        print('Число нечетное')

n = int(input('Введите целое число: '))

even_numbers(n)
