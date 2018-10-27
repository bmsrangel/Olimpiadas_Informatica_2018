m = []  # matriz
pc = []  # peso das colunas

def maiorPeso():
    pc.clear()
    for i in range(0, n):
        soma = 0
        for j in range(0, n):
            soma += m[j][i]
        pc.append(soma)


def pesoTotal(m):
    soma = 0
    for i in m:
        for j in i:
            soma += j
    return soma


n = int(input())

for i in range(0, n):
    m.append([])
    for j in range(0, n):
        m[i].append(int(input()))

for j in range(0, n):
    maiorPeso()
    col = pc.index(max(pc))
    for i in range(0, n - 1 - j):
        m[i][col] = 0

print(pesoTotal(m))
