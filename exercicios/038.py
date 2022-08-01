cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
print(cores['vermelho'],'* '*40, cores['limpa'])
print('                          Compara dois valores.')
print(cores['vermelho'],'* '*40, cores['limpa'])
n1 = int(input('Informe o 1° número inteiro: '))
n2 = int(input('Informe o 2° número inteiro: '))
if n1 > n2:
    print('O valores são: {} e {} e o {} é maior.'.format(n1, n2, n1))
elif n2 > n1:
    print('Os valores são: {} e {} e o {} é maior.'.format(n1, n2, n2))
else:
    print('O números são iguais.')
