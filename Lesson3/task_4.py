# создаем словарь из исходных выражений и их соответствующих значений
data_list_values = [17 / 2 * 3 + 2, 2 + 17 / 2 * 3, 19 % 4 + 15 / 2 * 3,
                    (15 + 6) - 10 * 4, 17 / 2 % 2 * 3 ** 3]
data_list_keys = ['17 / 2 * 3 + 2', '2 + 17 / 2 * 3', '19 % 4 + 15 / 2 * 3',
                  '(15 + 6) - 10 * 4', '17 / 2 % 2 * 3 ** 3']
data_dict = dict(zip(data_list_keys, data_list_values))

# расставили скобки
corr_expr = ['(17 / 2 * 3) + 2', '2 + (17 / 2 * 3)', '(19 % 4) + (15 / 2 * 3)',
             '(15 + 6) - (10 * 4)', '17 / 2 % 2 * (3 ** 3)']
corr_expr_values = [(17 / 2 * 3) + 2, 2 + (17 / 2 * 3), (19 % 4) +
                    (15 / 2 * 3), (15 + 6) - (10 * 4), 17 / 2 % 2 * (3 ** 3)]

index = 0

for expression, value in data_dict.items():
    print('Значение исходного выражения равняется:')
    print(expression, '=', value)

    print('Значение выражения со скобками равняется:')
    print(corr_expr[index], '=', corr_expr_values[index])
    if value == corr_expr_values[index]:
        print('Вы правильно расставили скобки!')
    else:
        print('Вы не правильно расставили скобки. Попробуйте еще раз.')
    index += 1
    print()
    print()
