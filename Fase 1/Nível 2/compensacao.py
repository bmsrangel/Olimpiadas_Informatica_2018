lista = list()
grafo = list()
saldo = list()
while True:
    m = int(input())  # total de cheques emitidos
    n = int(input())  # total de cidadãos
    if 1 <= m <= 1e6 and 2 <= n <= 1e3:
        break

for c in range(0, m):
    lista.append([])
    for d in range(0, 3):
        lista[c].append(int(input()))

for c in range(0, n):
    grafo.append([])
    saldo.append(0)

for c in range(0, m):
    grafo[lista[c][0] - 1].append(lista[c][2])

print(grafo)
