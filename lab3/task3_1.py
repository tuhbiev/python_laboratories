string = input('Введите строку: ')[:-1:]
symbol = input('Введите символ: ')
words = string.split(' ')
len_string = [len(word) for word in words]
string = string.replace(symbol, '')
string = [word*2 for word in string]

print('Длина строки: {}'.format(len(string)))
print('Слов в строке: {}'.format(len(words)))
print('Длина самого короткого слова: {}'.format(min(len_string)))
print('Длина самого длинного слова: {}'.format(max(len_string)))
print('Преобразованная: {}'.format(''.join(string)))
