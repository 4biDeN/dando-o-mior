c, b, p = map(int, input().split())
rc, rb, rp = map(int, input().split())
soma=0
if rc > c:
    soma += rc - c
if rb > b:
    soma += rb - b
if rp > p:
    soma += rp - p

print(soma)
