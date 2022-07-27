from random import shuffle
print('Este código sorteia ordem de apresentação de um trabalho.')
nomes = [input('Aluno 1: '), input('Aluno 2: '), input('Aluno 3: '), input('Aluno 4: ')]
shuffle(nomes)
print('A ordem da apresentação é: {}'.format(nomes))