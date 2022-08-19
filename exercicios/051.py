print('\033[31m* \033[m' * 40)
print('             Este código verificar a progressão aritmétrica.')
print('\033[31m* \033[m' * 40)
t = int(input('Informe o termo: '))
r = int(input('Informe a razão: '))
d = t + (10 - 1) * r
for x in range(t, d, r):
    print('{} '.format(x), end=' > ')
print('ACABOU')
