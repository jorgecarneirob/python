print('\033[31m* \033[m' * 40)
print('             Este código verificar se o número é primo.')
print('\033[31m* \033[m' * 40)
n = int(input('Informe o número a ser verificado: '))
mult = 0
for x in range(2, n):
    if (n % x) == 0:
        print('Multiplo de {}'.format(x))
        mult += 1
if (mult == 0):
    print('{} é primo'.format(n))

else:
    print('{} não é primo'.format(n))