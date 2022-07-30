print('Este programa calcula o valor de uma viajem.')
d = float(input('Digite a distância em KMs: '))
if d >=200:
    print('A distancia é: {}/n O valor para sua viajem é d: {}'.format(d, d*0.45))
else:
    print('A distancia é: {}/n O valor para sua viajem é d: {}'.format(d, d*0.50))