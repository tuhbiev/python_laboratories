import math

lmt = int(input('Введите лимит: ')) + 1
x = int(input('Введите x '))
list_num = list(range(0, lmt))
sum = 0

for index in range(lmt):
    sum = sum + (1/((2*index+1)*math.pow(x,2*index+1)))
    print(index)
print(sum)