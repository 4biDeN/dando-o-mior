soma = 0
positivos = 0
for i in range(6):
    x = float(input())
    if x > 0:
        soma += x
        positivos +=1
print('{} valores positivos\n{:.1f}'.format(positivos, (soma/positivos)))