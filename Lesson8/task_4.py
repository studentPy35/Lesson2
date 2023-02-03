'''4. Прочитать соxранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озоглавив каждый столбец и добавив новый столбец "телефон".'''

# Первый вариант

import json, csv

with open('create_dict.json', encoding='utf8') as file_in, open('csv_dict.csv', 'w', encoding='utf8') as file_out:
    decoding_object = json.load(file_in)
    decoding_lst_object = [[k, *v] for k, v in decoding_object.items()]
    [lst.append(input(f'Введите номер телефона для {lst[1]}: ')) for lst in decoding_lst_object]
    head_liners = ['id', 'Name', 'Age', 'Phone number']
    writer = csv.writer(file_out, delimiter=';')
    writer.writerow(head_liners)
    writer.writerows(decoding_lst_object)

# Второй вариант

# import json, csv
#
# with open('create_dict.json', encoding='utf8') as file_in, open('csv_dict.csv', 'w', encoding='utf8') as file_out:
#     decoding_object = json.load(file_in)
#     decoding_lst_object = [[k, *v] for k, v in decoding_object.items()]
#     [lst.append(input(f'Введите номер телефона для {lst[1]}: ')) for lst in decoding_lst_object]
#     head_liners = ['id', 'Name', 'Age', 'Phone number']
#     result = [dict(zip(head_liners, decoding_lst_object[i])) for i in range(len(decoding_object))]
#     writer = csv.DictWriter(file_out, fieldnames=head_liners, delimiter=';')
#     writer.writeheader()
#     writer.writerows(result)




