dist = int(input())
if dist <= 800:
    pontos = 1
else:
    if dist > 800 and dist <= 1400:
        pontos = 2
    else:
        if dist > 1400 and dist <= 2000:
            pontos = 3
print(pontos)