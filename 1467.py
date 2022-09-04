while (True):
    try:
        a, b, c = map(int, input().split())
        if a == b == c:
            print('*')
        else:
            if a == b != c:
                print('C')
            else:
                if a == c != b:
                    print('B')
                else:
                    if c == b != a:
                        print('A')
    except EOFError:
        break