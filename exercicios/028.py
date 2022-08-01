from random import randint
from time import sleep
print(' *'*10,'Este código sorteia um número para você adivinhar.',' *'*10)
print(' #' * 20)
print(' '*15,'SORTEANDO....')
print(' #' * 20)
sleep(3)
n = float(input('Fala um número de 0 a 5!: '))
r = randint(0,5)
print('o numero é: {}'.format(r))
print('Acertou miseravi'.upper() if n == r else 'Errou!'.upper())
