x = list(map(int, input().split()))
ordem = sorted(x)
print(*ordem, sep="\n")
print('', *x, sep="\n")
