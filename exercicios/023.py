print('Este código separa unidade, dezena, centena e milhar')
v = int(input('Digite um valor entre 0 e 9999: '))
u = v // 1 % 10
d = v // 10 % 10
c = v // 100 % 10
m = v // 1000 % 10
print('unidade: {}\ndezena: {}\ncentena: {}\nMilhar: {}'.format(u, d, c, m))