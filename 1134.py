lista = [0, 0, 0]
while(True):
    num = int(input())
    if num == 1:
        lista[0] += 1
    if num == 2:
        lista[1] += 1
    if num == 3:
        lista[2] += 1
    if num == 4:
        break
print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(lista[0],lista[1],lista[2]))