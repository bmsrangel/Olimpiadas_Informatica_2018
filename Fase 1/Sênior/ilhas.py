lista = []
while True:
    n = int(input())
    m = int(input())
    if 2 <= n <= 1000 and n-1 <= m <= 1e5:
        break

for c in range(0, m):
    lista.append([])
    for d in range(0, 3):
        lista[c].append(int(input()))

s = int(input())