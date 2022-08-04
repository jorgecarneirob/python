print('\033[31m* ' * 40, '\033[m')
print('                 Calcula a média e retorna o status.')
print('\033[31m* ' * 40, '\033[m')
n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média é: \033[31m{:.2f} REPROVADO.\033[m'.format(media))
elif media >= 7:
    print('Sua média é: \033[32m{:.2f} APROVADO!\033[m'.format(media))
else:
    print('Sua média é: \033[33m{:.2f} RECUPERAÇÃO.\033[m'.format(media))