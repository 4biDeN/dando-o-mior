import math
n = int(input())
resultado = (math.pow((1+math.sqrt(5)) / 2, n) - math.pow((1-math.sqrt(5)) / 2, n))/math.sqrt(5)
print('{:.1f}'.format(resultado))
