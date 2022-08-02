from datetime import date
print('\033[31m* \033[m' * 40)
print('                     Indica categoria por idade.')
print('\033[31m* \033[m' * 40)
nasc = int(input('Informe o ano de seu nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('Sua idade é: {} e você está na categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua idade é: {} e você está na categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é: {} e você está na categoria JUNIOR'.format(idade))
else:
    print('Sua idade é: {} e você está na categoria SENIOR'.format(idade))