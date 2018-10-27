l = int(input())
c = int(input())
if l < 1 or c < 1:
    print('Entrada deve ser maior que 0')
elif l > 1000 or c > 1000:
    print('Entrada deve ser menor que ou igual a 1000')
else:
    if l % 2 == 1 and c % 2 == 1 or l % 2 == 0 and c % 2 == 0:
        print(1)
    else:
        print(0)
