'''1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем
результат преобразовать в байтовый вид в кодировке ‘Latin1’ и затем результат
снова декодировать в строку (результаты всех преобразований выводить на экран).'''

text = b'r\xc3\xa9sum\xc3\xa9'
str_text = text.decode()                             # декодируем байтовое значение в строку
print(str_text)

latin_text = str_text.encode('Latin1')               # преобразовываем в байтовый вид в кодировке ‘Latin1’
print(latin_text)

decoding_latin_text = latin_text.decode('Latin1')    # декодируем байтовое значение в строку
print(decoding_latin_text)
