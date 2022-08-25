print('\033[31m* \033[m' * 50)
print('''Este código usa while
Para verificar o sexo.'''.center(100))
print('\033[31m* \033[m' * 50)
sexo = 'm'
while sexo in 'MmFf':
    sexo = input('Digite [M/F]').strip()
    print(sexo)
