x = int(input('Вес шоколадных конфет = '))
a = int(input('Стоимость шоколадных конфет = '))
y = int(input('Вес ирисок = '))
b = int(input('Стоимость ирисок = '))

if a > 0 and x > 0:
    print('Цена 1 кг шоколадных конфет: {} рублей'.format(float(a / x)))
elif a < 0:
    print('Стоимость не может быть меньше 0')
elif x < 0:
    print('Вес не может быть меньше 0')

if y > 0 and b > 0:
    print('Цена 1 кг ирисок: {} рублей'.format(float(b / y)))
elif b < 0:
    print('Стоимость не может быть меньше 0')
elif y < 0:
    print('Вес не может быть меньше 0')

if (a/x) > (b/y):
    print('Шоколадные конфеты дороже в {} раза'.format(round((a/x)/(b/y))))
elif (a/x) > (b/y):
    print('Ириски дороже в {} раз'.format(round((b/y)/(a/x))))
else:
    print('Стоимость равна.')
