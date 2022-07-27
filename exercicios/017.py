from math import hypot
print('Este codigo retorna a hipotenusa dos catetos')
o = float(input('Informe o cateto oposto: '))
a = float(input('Informe o cateto ajacente: '))
print('O valor da hipotenusa é: {:.2f}'.format(hypot(o ,a)))