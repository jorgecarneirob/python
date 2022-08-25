print('\033[31m* \033[m' * 50)
print('''Este código usa while Para verificar o sexo.'''.center(100))
print('\033[31m* \033[m' * 50)
sexo = input('Digite [M/F]').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('\033[31m[ \033[mERRO\033[31m ]\033[m Digite uma valor válido.\n Digite [M/F]').strip().upper()[0]
print('Sexo {} registadro'.format(sexo))