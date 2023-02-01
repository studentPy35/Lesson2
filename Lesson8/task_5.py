import csv
from openpyxl import Workbook
from openpyxl.styles import Font
# создаем файл, активируем лист
wb = Workbook()
ws = wb.active
# открываем csv файл и считываем в переменную его содержимое с виде список списков
with open('csv_dict.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=';'))
# записываем поочередно каждую строку
for row in reader:
    ws.append(row)
# удаляем третий столбец Age
ws.delete_cols(3)
# делаем полужирный шрифт в первой строке (названия столбцов)
ft = Font(bold=True)
for row in ws["A1:C1"]:
    for cell in row:
        cell.font = ft

# сохраняем файл как "task_55.xlsx"
wb.save("task_55.xlsx")
wb.close()