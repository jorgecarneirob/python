print('\033[31m* \033[m' * 40)
print('Este código exibe a tabuada de um numero inteiro.')
print('\033[31m* \033[m' * 40)
n = int(input('Digite um numero inteiro: '))
vezes = int(input('Até qual tabuada?: '))
for t in range(0, vezes+1):
    r = t * n
    print('{} x {} = {}'.format(n, t, r))
