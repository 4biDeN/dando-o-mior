x = int(input())
qtde_in = 0
qtde_out = 0
for i in range(x):
    y = int(input())
    if y >= 10 and y <= 20:
        qtde_in += 1
    else:
        qtde_out += 1
print('{} in\n{} out'.format(qtde_in, qtde_out))