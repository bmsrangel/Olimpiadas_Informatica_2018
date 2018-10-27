x = set()
n = int(input())
m = int(input())
for c in range(0, m):
    x.add(input())
print(n - len(x))
