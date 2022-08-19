print('\033[31m* \033[m' * 40)
print('             Este código verificar se o número é primo.')
print('\033[31m* \033[m' * 40)
n = int(input('Informe o número a ser verificado: '))
mult = 0
for x in range(1, n+1):
    if (n % x) == 0:
        print('Multiplo de \033[33m{}\033[m'.format(x))
        mult += 1
if (mult == 0):
    print('\033[33m{}\033[m é primo'.format(n))
else:
    print('\033[33m{}\033[m não é primo'.format(n))