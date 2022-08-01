cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
print(cores['vermelho'],'* '*40, cores['limpa'])
print('                 Este código é sobre funções aninhadas.')
print(cores['vermelho'],'* '*40, cores['limpa'])
nome = str(input('Digite o seu nome: '))
if nome == 'Fer' or nome == 'Fernanda':
    print('{}Seja bem vinda mestra!'.format(cores['vermelho']))
elif nome == 'Jorge' or nome == 'Jorginho':
    print('{}Seja bem vindo mestre!'.format(cores['azul']))
else:
    print('{}Seja bem vindo!:{} {}'.format(cores['amarelo'], cores['limpa'], nome))