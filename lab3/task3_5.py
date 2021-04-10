import random
#import numpy as np
matrix_n = int(input('Введите n:'))
matrix_m = int(input('Введите m:'))

matrix_rand = [[randint(1,100) for k in range(matrix_n)] for j in range(matrix_m)]
#matrix_rand = np.random.randint(0, 100, size=(matrix_n, matrix_m))
chet = 0
nechet = 0
matrix_list = matrix_rand.ravel().tolist()
for i in range(len(matrix_list)):
    if i % 2 == 0:
        chet += 1
    else:
        nechet +=1
print(matrix_rand)
print(matrix_list)
print('Количество четных чисел: {}'.format(chet))
print('Количество нечетных чисел: {}'.format(nechet))
