n =int(input())
for i in range(n+1):
    if i > 0 and i % 2 == 0:
        print('{}^{} = {}'.format(i, 2, (i*i)))