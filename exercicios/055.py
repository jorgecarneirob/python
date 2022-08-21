print('\033[31m* \033[m' * 50)
print('Este código faz uma anáise completa.'.center(100))
print('\033[31m* \033[m' * 50)
nomeh = ''
idadeh = 0
idadem = 0
idadeg = 0
for x in range(1, 5):
    nome = str(input('Qual o seu nome?: '))
    idade = int(input('Qual sua idade?: '))
    sexo = str(input('Digite M para mulher ou H para Homem: '))
    if x == 1 and sexo == 'H':
        nomeh = nome
        idadeh = idade
        idadeg += idade
    if idade > idadeh and sexo == 'H':
        nomeh = nome
        idadeh = idade
        idadeg += idade
    if sexo == 'M' and idade < 20:
        idadeg += idade
        idadem +=1
idadeg = idadeg / 4
print('''A média de idade do grupo é:{}
O homem mais velho é o: {}
{} mulheres tem menos de 20 anos.'''.format(idadeg, nomeh, idadem))

