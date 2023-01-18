# программа для вывода последовательности из n чисел Фибоначчи
import timeit

n = int(input('Введите число: '))

# воспользовались рекурсивной функцией
def fibonacci_number(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_numbers_1(n):
    fibonacci_list = []
    for i in range(1, n + 1):
        fibonacci_list.append(fibonacci_number(i))
    return fibonacci_list


# использовали циклы для решения задачи
def fibonacci_numbers_2(n):
    index = 1
    fibonacci_list = []
    previous_number_1 = 0
    previous_number_2 = 1
    while n + 1 > index:
        if index == 1:
            fibonacci_list.append(previous_number_1)
        elif index == 2:
            fibonacci_list.append(previous_number_2)
        else:
            fibonacci_list.append(previous_number_1 + previous_number_2)
            previous_number_1, previous_number_2 = previous_number_2, previous_number_2 + previous_number_1
        index += 1
    return fibonacci_list


print(*fibonacci_numbers_1(n))
print(*fibonacci_numbers_2(n))

# используем модуль timeit для определения времени выполнения программ
fibonacci_time_1 = timeit.timeit(lambda: fibonacci_numbers_1(n))
fibonacci_time_2 = timeit.timeit(lambda: fibonacci_numbers_2(n))

print('Используя рекурсивную функцию и range: ', fibonacci_time_1)
print('Используя циклы: ', fibonacci_time_2)

if fibonacci_time_1 > fibonacci_time_2:
    print('Лучше использовать циклы')
elif fibonacci_time_1 < fibonacci_time_2:
    print('Лучше использовать рекурсивную функцию')
else:
    print('Используйте то, что Вам больше нравится')