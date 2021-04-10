n = int(input('Введите число: '))
numbers = []
for i in range(n + 1):
    numbers.append(i)
numbers[1] = 0
i = 2
while i <= n:
    if numbers[i] != 0:
        j = i + i
        while j <= n:
            numbers[j] = 0
            j = j + i
    i += 1

numbers = set(numbers)
numbers.remove(0)
print(numbers)

num_list = [x for x in range(1, n) if x % 7 == 0]
print(num_list)
