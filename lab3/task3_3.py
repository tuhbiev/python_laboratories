import random

num = int(input('Входное значение чисел элементов в списке: '))
num_list = sorted([random.randint(-500, 500) for x in range(0, num)])
num_list = [10, 10, 11, 11, 15, 16, 17]
index = num_list.index(min(num_list))
res = num_list[:index]
for i in range(index if index % 2 else index+1, len(num_list),2):
   if i>0:
      res.append(i)

print(res)
