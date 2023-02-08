from collections import Counter

"""Программа для подсчета количества букв в тексте"""
with open('test.txt', encoding='utf8') as file:
    text = filter(lambda x: x.isalpha(), file.read().lower())
    letter = input('Введите любую английскую букву: ').lower()
    print(f'Буква встречается {Counter(text)[letter]} раз(а) в тексте')
