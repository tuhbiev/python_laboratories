import math

a = float(input("R1 = "))
b = float(input("R2 = "))

if a>0 and b>0:
   print('Площадь первого круга = {}'.format(round(math.pi ** 2 * a)))
   print('Площадь второго круга = {}'.format(round(math.pi ** 2 * b)))
   print('Площадь кольца = {}'.format(round(math.pi * (b ** 2 - a ** 2))))
else:
   print("Радиус не может быть меньше 0")
