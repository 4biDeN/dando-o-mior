x = int(input())
h = x // 3600
rest_horas = x % 3600
m = rest_horas // 60
s = rest_horas % 60
print('{}:{}:{}'.format(h, m, s))