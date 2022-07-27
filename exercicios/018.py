from math import sin, cos, tanh, radians
a = float(input('Informe o ângulo: '))
print('O seno é:{:.2f}\nO cosseno é: {:.2f} \nA tangente é: {:.2f}'
.format(sin(radians(a)),(cos(radians(a))), (tanh(radians(a)))))
