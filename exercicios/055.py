print('\033[31m* \033[m' * 50)
print('Exibe o maior e o menor peso.'.center(100))
print('\033[31m* \033[m' * 50)
maior = 0
menor = 0
p = ''
cont = 1
while p in 'Yy':
    peso = float(input('Digite seu peso Kg: '))
    if cont == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    cont += 1
    p = input('Deseja continuar?[y/n]: ')
print('''Maior peso: {}Kg.
Menor: {}Kg'''.format(maior, menor))