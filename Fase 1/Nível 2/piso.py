while True:
    l = int(input())
    c = int(input())
    if 1 <= l <= 100 and 1 <= c <= 100:
        break

t1 = l * c + ((l - 1) * (c - 1))
t2 = 2 * (l - 1) + 2 * (c - 1)

print(t1)
print(t2)