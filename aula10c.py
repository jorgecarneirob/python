print('Este código mostra resultado do ano letivo: ')
n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
r = (n1 + n2) / 2
print('Sua média foi: '.format(r))
print('Aprovado' if r >= 5 else 'Reprovado')
#if r <= 5:
#    print('Reprovado')
#else:
#    print('Aprovado')
