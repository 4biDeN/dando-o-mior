A, B, C = map(float, input().split())
if abs(B - C) < A < (B + C) and (A - C) < B < (A + C) and (A - B) < C <(A + B):
    perimetro = A + B + C
    print('Perimetro = {}'.format(perimetro))
else:
    area = (A+B)*C/2
    print('Area = {}'.format(area))