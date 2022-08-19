from time import sleep
print('\033[31m* \033[m' * 40)
print('                         Exibe numeros pares ou impares.')
print('\033[31m* \033[m' * 40)
fim = int(input('Informe um número inteiro final: '))
escolha = int(input('''[ 1 ] IMPAR
[ 2 ] PAR
Digite a opção: '''))
for x in range(0, fim):
    if escolha == 1 and (x % 2) == 0:
        print(x + 1, end=' ')
    elif escolha == 2 and (x % 2) != 0:
        print(x + 1, end=' ')
if escolha != 1 and escolha != 2:
    print ('[ \033[31mERRO\033[m ] OPÇÂO INVALIDA')
