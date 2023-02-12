from collections import Counter

"""There is a program for counting the number of letters in a text"""
with open('test.txt', encoding='utf8') as file:
    letter = input('Enter a letter: ').lower()
    count = 0
    for line in file:
        text = filter(lambda x: x.isalpha(), line.lower())
        count += Counter(text)[letter]
    print(f'The letter occurs {count} times in the text')
