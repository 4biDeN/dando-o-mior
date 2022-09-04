A, B, C = map(float, input().split())
X = float()
if (A < B):
    X = A
    A = B
    B = X
if (B < C):
    X = B
    B = C
    C = X
if (A < B):
    X = A
    A = B
    B = X
if A >= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    else:
        if A**2 > B**2 + C**2:
            print('TRIANGULO OBTUSANGULO')
        else:
            if A**2 < B**2 + C**2:
                print('TRIANFULO ACUTANGULO')
if A == B and B == C:
    print('TRIANGULO EQUILATERO')
else:   
    if A == B or B == C:
        print('TRIANGULO ISOSCELES')