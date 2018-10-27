carimbadas = list()
compradas = list()
tot = 0
while True:
    n = int(input())
    c = int(input())
    m = int(input())
    if 1 <= n <= 100 and 1 <= c <= n / 2 and 1 <= m <= 300:
        break

for cont in range(0, c):
    carimbadas.append(int(input()))
for cont in range(0, m):
    compradas.append(int(input()))
for i in carimbadas:
    if i in compradas:
        tot += 1

print(len(carimbadas) - tot)