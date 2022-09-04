qtde, tam_muralha = input().split()
tipo_tita = input()
tam_P, tam_M, tam_G = input().split()

muralhas = [int(tam_muralha)]*int(qtde)
tp, tm, tg = [0, 0, 0]

for i in tipo_tita:
    if i == 'P':
        while muralhas[tp] < int(tam_P):
            tp += 1
        muralhas[tp] -= int(tam_P)    
    elif i == 'M':
        while muralhas[tm] < int(tam_M):
            tm += 1
        muralhas[tm] -= int(tam_M)
    elif i == 'G':
        while muralhas[tg] < int(tam_G):
            tg += 1
        muralhas[tg] -= int(tam_G)

print(max(tp, tm, tg)+1)