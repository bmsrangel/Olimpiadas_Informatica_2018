n = int(input())  # Tamanho da sequência de números
x = str(input()).split(' ')  # Sequência de números
for c in range(0, n):
    x[c] = int(x[c])  # Separação e conversão da entrada string para lista de inteiros
c = 1
if n > 1:
    a = x[1] - x[0]
    for i in range(1, n):
        if (x[i] - x[i-1]) != a:
            c += 1
            a = x[i] - x[i-1]
print(c)
