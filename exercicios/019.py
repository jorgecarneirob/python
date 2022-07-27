from random import choice
print('Este código sorteia um aluno.')
nomes = [input('Aluno 1: '), input('Aluno 2: '), input('Aluno 3: '), input('Aluno 4: ')]
print('O sorteado é: {}'.format((choice(nomes))))