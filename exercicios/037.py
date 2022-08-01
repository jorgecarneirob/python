from time import sleep
cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
print(cores['vermelho'],'* '*40, cores['limpa'])
print('                          Conversor de base numérica.')
print(cores['vermelho'],'* '*40, cores['limpa'])
numero = int(input('Informe um número inteiro: '))
