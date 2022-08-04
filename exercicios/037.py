from time import sleep
cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
print(cores['vermelho'],'* '*40, cores['limpa'])
print('                          Conversor de base numérica.')
print(cores['vermelho'],'* '*40, cores['limpa'])
numero = int(input('Informe um número inteiro: '))
base = int(input('''[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
Informe para qual base deseja converter: '''))
if base == 1:
    print('{} convertido em BINÁRIO é: {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é: {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é: {}'.format(numero, hex(numero)[2:]))
else:
    print('[ \033[31mERRO\033[m ] Opção inválida!')