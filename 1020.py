idade = int(input())
anos = idade // 365
meses_rest = idade % 365
meses = meses_rest // 30
dias = meses_rest % 30
print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')