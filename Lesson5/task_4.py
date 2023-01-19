n = int(input('Введите целое число n: '))

# применили цикл for
total = 0
for i in range(1, n + 1):
    total += i ** 3

print(f'Сумма кубов целых чисел от 1 до n: {total}')

# применили цикл while
total = 0
while n > 0:
    total += n ** 3
    n -= 1

print(f'Сумма кубов целых чисел от 1 до n: {total}')


