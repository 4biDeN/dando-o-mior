x = int(input())
c_100 = x // 100
resto_100 = x % 100
c_50 = resto_100 // 50
resto_50 = resto_100 % 50
c_20 = resto_50 // 20
resto_20 = resto_50 % 20
c_10 = resto_20 // 10
resto_10 = resto_20 % 10
c_5 = resto_10 // 5
resto_5 = resto_10 % 5
c_2 = resto_5 // 2
resto_2 = resto_5 % 2
c_1 = resto_2 // 1

print('NOTAS:')
print(c_100, 'nota(s) de R$ 100,00')
print(c_50, 'nota(s) de R$ 50,00')
print(c_20, 'nota(s) de R$ 20,00')
print(c_10, 'nota(s) de R$ 10,00')
print(c_5, 'nota(s) de R$ 5,00')
print(c_2, 'nota(s) de R$ 2,00')
print(c_1, 'nota(s) de R$ 1,00')