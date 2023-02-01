'''2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
строки, каждая из которых должна начинаться с новой строки.'''

string_1, string_2, string_3, string_4 = input(), input(), input(), input()

# создаем файл и записываем в него первые 2 переменные
with open('study_files.txt', 'w', encoding='utf8') as output_file:
    print(string_1, file=output_file)
    print(string_2, file=output_file)

# открываем файл для редактирования и записываем в него оставшиеся 2 переменные
with open('study_files.txt', 'a', encoding='utf8') as output_file:
    print(string_3, file=output_file)
    print(string_4, file=output_file)

