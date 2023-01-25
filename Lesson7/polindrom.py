from beartype import beartype

@beartype
def polindrom(words: tuple) -> tuple:
    '''Функция принимает кортеж слов и возвращает кортеж, состоящий из полиндромов'''
    return tuple(filter(lambda word: word == word[::-1], words))

words = ('собака', 'abba', 'wolf', 'level', 'apple', 'madam', 'sun', 'шалаш', 'комок')
print(polindrom(words))