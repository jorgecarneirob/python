print('Este programa calcula o valor de uma viajem.')
d = float(input('Digite a distância em KMs: '))
if d <=200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('A distancia é: {}/n O valor para sua viajem é d: {}'.format(d, preco))