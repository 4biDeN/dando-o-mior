v1 = int(input())
v2 = int(input())
soma = 0
if v1 > v2:
    for y in range(v2+1, v1):
        if y % 2 == 1:
            soma = soma + y
else:
    for y in range(v1, v2):
        if y % 2 == 1:
            soma = soma + y
print(soma)