num = []
cont = 0
for x in range(6):
    x = float(input())
    num.append(x)
    if x > 0:
        cont = cont + 1
print('{} valores positivos'.format(cont))