d = int(input())
if d < 0:
    print('Distância inválida!')
elif d <= 800:
    print(1)
elif d <= 1400:
    print(2)
elif d <= 2000:
    print(3)
else:
    print('Distância inválida! O limite é 2000cm')