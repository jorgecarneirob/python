from termcolor import colored
#cores = ['limpad':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m']
print(colored('* '*40,'red'), 
colored('\nEste código verifica se é possível montar um triangulo.\n', 'green'), 
colored('* '*40,'red'))
a = float(input('Informe o 1° valor: '))
b = float(input('Informe o 2° valor: '))
c = float(input('Informe o 3° valor: '))

if a < b + c and b < a + c and c < a + b:
    print(colored('ESTES VALORES FORMAM UM TRIANGULO!','green'))
else:
    print(colored('ESTE VALORES NÃO FORMAM UM TRIANGULO','red'))