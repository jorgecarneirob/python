from time import sleep
print('\033[31m* \033[m' * 40)
print('                         Exibe numeros pares ou impares.')
print('\033[31m* \033[m' * 40)
fim = int(input('Informe um número inteiro final: '))
escolha = int(input('''[ 1 ] PAR
[ 2 ] IMPAR
Digite a opção: '''))
for x in range(0, fim):
    if escolha == 1 and (x // 2) == 0:
        print(x + 1)