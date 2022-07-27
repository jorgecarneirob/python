print('Este código mostra o dobro o triplo e a raiz quadrada do input(inteiro).')
i = int(input('Digite um núemro inteiro: '))
d = i*2
t = i*3
r = i**(1/2)
print('O número inteiro é: {}\n o dobro é: {}\n o triplo é: {}\n e a raiz é: {:.2f}'.format(i, d, t, r))