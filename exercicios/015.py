print('Este código calcula o aluguel de um carro')
km = float(input('Informe a quantidade de KM rodados: '))
dia = int(input('Informe a quantidade de dias alugados: '))
vdia = 60
vkm = 0.15
print('KMs rodados: {} dias {} total: {}'.format(km, dia, dia*vdia + km*vkm))