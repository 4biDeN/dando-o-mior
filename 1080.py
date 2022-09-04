num = []
while len(num) < 100:
    x = int(input())
    num.append(x)
maior = max(num)
posicao = num.index(maior) + 1 
print('{}\n{}'.format(maior, posicao))