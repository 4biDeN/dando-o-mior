pares = []
impares = []
n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
pares.sort()
impares.sort(reverse=True)
print(*pares, sep="\n")
print(*impares, sep="\n")