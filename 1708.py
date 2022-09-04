import math

rapido, lento = map(int, input().split())

x = lento - rapido
voltas = math.ceil(int(lento)/x)
print(voltas)