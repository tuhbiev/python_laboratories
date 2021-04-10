import random

def series(iter_, func):
   result = []
   a_list = []
   for e in iter_:
      if func(e):
         a_list.append(e)
      elif a_list:
         result.append(a_list)
         a_list = []
   return result

num = int(input('Входное значение чисел элементов в списке: '))
num_list = [random.randint(-500, 500) for x in range(0, num)]
num_mass = num_list
print(num_mass)

negatives = series(num_list, lambda x: x < 0)
max_serie = max(negatives)

for e in range(len(num_list) - len(max_serie)):
   if num_list[e: e + len(max_serie)] == max_serie:
      del num_list[e: e + len(max_serie)]
num_list.extend(max_serie)


print(num_list)
