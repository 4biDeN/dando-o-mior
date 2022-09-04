x = int(input())
lista = []
for y in range(x):
    num = int(input())
    if num == 0:
        lista.append('NULL')
    else:
        if num > 0 and num % 2 == 0:
            lista.append('EVEN POSITIVE')
        else:
            if num < 0 and num % 2 == 0:
                lista.append('EVEN NEGATIVE')
            else:
                if num > 0 and num % 2 == 1:
                    lista.append('ODD POSITIVE')
                else:
                    if num < 0 and num % 2 == 1:
                        lista.append('ODD NEGATIVE')
print(*lista, sep="\n")
