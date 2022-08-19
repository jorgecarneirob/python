from datetime import date
print('\033[31m* \033[m' * 40)
print('         Este código verificar maiores de idade.')
print('\033[31m* \033[m' * 40)
maior = 0
menor = 0
hoje = date.today().year
for x in range(1, 8):
    ano = int(input('Informe a {}° data: '.format(x)))
    if hoje - ano >= 18:
        maior += 1
    else:
        menor += 1
print('''Pelos nascimentos informados:
{} são maiores de idade
{} são menores de idade'''.format(maior, menor))