import math
voltas, placas = map(int, input().split())

total_placas = ((voltas*placas)/100)
#float(total_placas)
lst = []

for i in range(1, 10):
    if voltas == 10:
        resultado = math.floor(total_placas*(i*10))
        lst.append(resultado)
    else:
        resultado = math.ceil(total_placas*(i*10))
        lst.append(resultado)
print(*lst, sep=' ')
