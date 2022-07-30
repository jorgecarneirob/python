import random
n = float(input('Fala um número de 0 a 100!: '))
r = random.randint(0,100)
print('o numero é: {}'.format(r))
print('Acertou miseravi' if n == r else 'Errou!')
