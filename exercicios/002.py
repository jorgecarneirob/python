cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
nome = input ('Qual o seu nome?')
print ('{}Seja bem vindo{} ,{}{}{}!'.format(cores['azul'],
cores['limpa'],cores['vermelho'], nome, cores['limpa']))