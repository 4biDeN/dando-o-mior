coelho = 0
sapo = 0
rato = 0
x = int(input())
for i in range(x):
    qtde, tipo = input().split()
    
    if tipo == 'C':
        coelho = int(qtde) + coelho
    if tipo == 'R':
        rato = int(qtde) + rato
    if tipo == 'S':
        sapo = int(qtde) + sapo
    
    total_cobaias = coelho + rato + sapo

    percent_coelho = (coelho/total_cobaias) * 100
    percent_rato = (rato/total_cobaias) * 100
    percent_sapo = (sapo/total_cobaias) * 100

print('Total: {} cobaias'.format(total_cobaias))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format(percent_coelho))
print('Percentual de ratos: {:.2f} %'.format(percent_rato))
print('Percentual de sapos: {:.2f} %'.format(percent_sapo))