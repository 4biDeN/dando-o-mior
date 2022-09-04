linhas = int(input())
colunas = int(input())
if colunas % 2 == 0 and linhas % 2 == 0:
    print(1)
else:
    if colunas % 2 == 1 and linhas % 2 == 1:
        print(1)
    else:
        print(0)