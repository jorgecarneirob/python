print(' *'*10,'Este código verifica a velocidade do carro e calcula multa.',' *'*10)
v = float(input('Informe a velocidade de carro: ''KM/H: '))
if v > 80:
    print('Você excedeu o limite em: {} KM/H e pagará uma multa de R$: {:.2f}'.format(v - 80,(v - 80) * 7))
else:
    print('No limite')