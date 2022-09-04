A, B = map(int, input().split())
if A < B:
    t = B - A
else:
    t = (24 - A) + B
print('O JOGO DUROU', t, 'HORA(S)')