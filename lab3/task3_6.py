from random import randint
mass = [[[randint(1,100) for k in range(7)] for j in range(5)] for i in range(3)]
elemmax = mass[0][0][0]
for i in range(3) :
    for j in range(5) :
        print(*mass[i][j])
        emax = max(mass[i][j])
        if emax > elemmax:
            elemmax = emax
            km = mass[i][j].index(emax)
            kj = j
            ki = i
    print()
print(ki, kj, km)
print('Наибольшее число: {}'.format(elemmax))
