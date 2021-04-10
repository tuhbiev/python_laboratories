import random

def seria(x, element):
    for x in element:
        resault = []
        el_list = []
        if x%2 != 0:
            resault.append(x)
        elif el_list:
            el_list(x)
            resault = []
        return resault

mass_element = int(input('Количество элементов в списке = '))
a = int(input('Диапозон начало = '))
b = int(input('Диапозон конец = '))

mass_list = [random.randint(a, b) for i in range(0, mass_element)]
print(mass_list)

itog_list = seria(mass_list, lambda x:x>0)
    
print(mass_element)
    
    