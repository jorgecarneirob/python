print('\033[31m* \033[m' * 50)
print('Este código faz uma anáise completa.'.center(100))
print('\033[31m* \033[m' * 50)
nomeh = ''
idadeh = 0
idadem = 0
idadeg = 0
cont = 1
while cont <= 4:
    print('\n====== {} PESSOA ====='.format(cont))
    nome = str(input('Qual o seu nome?: ')).strip().title()
    idade = int(input('Qual sua idade?: '))
    sexo = str(input('Sexo[M/H]: ')).strip()
    cont +=1
    if cont == 1 and sexo in 'Hh':
        nomeh = nome
        idadeh = idade
        idadeg += idade
    if idade > idadeh and sexo in 'Hh':
        nomeh = nome
        idadeh = idade
        idadeg += idade
    if sexo in 'Mn' and idade < 20:
        idadeg += idade
        idadem +=1
idadeg = idadeg / 4
print('''A média de idade do grupo é:{}
O homem mais velho é o: {}
{} mulheres tem menos de 20 anos.'''.format(idadeg, nomeh, idadem))