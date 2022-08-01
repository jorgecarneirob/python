from datetime import date
print('* '*20,'Este código verifica ano bissexto.','* '*20)
ano = int(input('\nDigite o ano ou 0 para ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}\nO ano é: {} e ele é BISSEXTO;\n{}'.format('# '*40, ano, '# '*40))
else:
    print('{}\nO ano é: {} e ele NÃO BISSEXTO;\n{}'.format('# '*40, ano, '# '*40))