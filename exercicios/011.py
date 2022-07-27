print('Este código calcula quantos litros de tinta para uma parede.')
l = float(input('Digite a altura da parede: '))
a = float(input('Digite a largura da parede: '))
area = l*a
t = area/2
print('Area em é: {} m² e a quantidade de tinta: {} lts'.format(area, t))