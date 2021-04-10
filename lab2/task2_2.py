fraza = input('Введите фразу содержащую от 10 символов: ')
if len(fraza) >= 10:
    print(fraza[0:4])
    print(fraza[-4:])
    print(fraza[int(len(fraza) / 2) - 1])
    print(fraza[2:8])
else:
    print('Необходимо ввести фразу от 10 символов.')
