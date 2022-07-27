from math import trunc
print('Este código retorna um inteiro de um número real.')
n = float(input('Digite um número real: '))
print('O real digitador é: {}.\nO inteiro dele é: {}'.format(n, (trunc(n))))
#print('O real digitador é: {}.\nO inteiro dele é: {}'.format(n, int(n)))