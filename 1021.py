x = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for nota in notas:
    qtde_nota = int(x / nota)
    print('{} nota(s) de R$ {:.2f}'.format(qtde_nota, nota))
    x -= qtde_nota * nota

print('MOEDAS:')
for moeda in moedas:
    qtde_moeda = int(round(x,2) / moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(qtde_moeda, moeda))
    x -= qtde_moeda * moeda