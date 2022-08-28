from time import sleep
print('\033[31m* \033[m' * 50)
print('''Este código faz funões matemáticas.'''.center(100))
print('\033[31m* \033[m' * 50)
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
resposta = 0
while resposta != 5:
    resposta = int(input('''
[ 1 ] SOMA
[ 2 ] MAIOR
[ 3 ] MULTIPLICAÇAO
[ 4 ] NOVO NUMEROS
[ 5 ] SAIR
Digite a opção:'''))
    if resposta == 1:
        print('A soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))
    elif resposta == 2 and n1 > n2:
        print('O maior entre {} e {} é {}'.format(n1, n2, n1))
    elif resposta == 2 and n1 < n2:
        print('O maior entre {} e {} é: {}'.format(n1, n2, n2))
    elif resposta == 2 and n1 == n2:
        print('{} e {} São IGUAIS!'.format(n1, n2))
    elif resposta == 3:
        print('A multiplicação de {} e {} é: {}'.format(n1, n2, n1 * n2))
    elif resposta == 4:
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    else:
        print('[ ERRO ] OPÇÃO INVALIDA.')
print('Saindo.', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.', end='')
sleep(1)
print('.',end='')