teste = int(input())

for i in range(teste):
    t1 = 0
    t2 = 1
    n = int(input())
    if n == 0:
        print('Fib({}) = {}'.format(n, t1))
        calls = 0 
    else:
        if n == 1 or n == 2:
            print('Fib({}) = {}'.format(n, t2))
        else:
            cont = 2   
            while cont <= n:
                calls += 2
                t3 = t1 + t2
                t1 = t2
                t2 = t3
                cont += 1
            
            print('Fib({}) = {}'.format(n, t3))