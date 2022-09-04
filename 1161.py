while(True):
    try:    
        n1, n2 = map(int, input().split())
        fatorial1 = 1
        fatorial2 = 1
        i = 2
        j = 2
        while i <= n1:
            fatorial1 = fatorial1 * i
            i = i + 1
        while j <= n2:
            fatorial2 = fatorial2 * j
            j += 1
        print(fatorial1 + fatorial2)
    except EOFError:
        break