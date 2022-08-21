print('\033[31m* \033[m' * 50)
print('''Este código usa while
Para verificar o sexo.'''.center(100))
print('\033[31m* \033[m' * 50)
#r = ''
sexo = input('Digite [M/F]')
while sexo in != 'MmFf':
    print('\033[31m[ \033[mERRO\033[31m ]\033[m Digite uma valor válido.')
print(sexo)
