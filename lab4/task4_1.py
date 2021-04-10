def read_graph():
    read = input("Ввести граф (y/n)? ")
    if read == "n":
        g = [[1, 1, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0],
             [0, 0, 0, 0, 2, 0, 0]]
        return [7, 6, g]
    n = int(input("Количество вершин n <= 7: "))
    k = int(input("Количество ребер k <= 28: "))
    g = [[0] * n] * k  # Матрица инцидентности
    for edge in range(k):
        print("Ребро ", edge, ": вершина с весом - ", end='')
        vrt1, vrt2, weight = input().split()
        vrt1 = int(vrt1)
        vrt2 = int(vrt2)
        weight = int(weight)
        if vrt1 == vrt2:
            weight *= 2
        g[i][vrt1] = weight
        g[i][vrt2] = weight
    return [n, k, g]


graph = read_graph()
N = graph[0]
K = graph[1]
G = graph[2]
print("\nМатрица инцидентности:")
for i in range(K):
    print(G[i])

print("\na) Для каждой вершины напечатать список инцидентных ей ребер:")
a = {}
for j in range(N):
    a[j] = []
    for i in range(K):
        if G[i][j] > 0:
            a[j].append(i)
print(a)

print("\nб) Определить степень каждой вершины графа:")
a = {}
for j in range(N):
    a[j] = 0
    for i in range(K):
        if G[i][j] > 0:
            a[j] += 1
print(a)

print("\nв) Проверить, есть ли вершины со степенью 0:")
b = [j for j in range(N)]
for j in range(N):
    if a[j] > 0:
        b.remove(j)
if len(b) == 0:
    print("Нет вершин со степенью 0.")
else:
    print("Есть вершины со степенью 0: ", b, ".")

print("\nг) Определить число вершин, инцидентных только одному ребру: ", end='')
count = 0
for j in range(N):
    if a[j] == 1:
        count += 1
print(count, ".")

print("\nд) Определить наибольшее число смежных между собой ребер, "
      "инцидентных одной и той же вершине: ", end='')
max_edge = a[0]
for j in range(1, N):
    if a[j] > max_edge:
        max_edge = a[j]
print(max_edge, ".")

print("\nе) Проверить, есть ли в графе петли:")
b = []
for j in range(N):
    for i in range(K):
        if G[i][j] == 2:
            b.append(i)
if len(b) == 0:
    print("Нет в графе петли.")
else:
    print("Есть в графе петля, список петель: ", b, ".")
