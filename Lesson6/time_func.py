from datetime import datetime
import time

def decorator(func):
    ''' Это сам декоратор'''
    def wrapper():
        print('Завернули функцию в обертку')
        time.sleep(2)
        print('Сейчас выполнится функция')
        test = func()
        time.sleep(2)
        print('Завершили')
        return test
    return wrapper


def get_time() -> str:
    a = datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')
    time.sleep(1)
    return a


@decorator  #декоратор
def get_generator() -> list:
    n = int(input('Введите количество элементов в генераторе: '))
    a = [get_time() for i in range(n)]
    return a


print(get_generator())