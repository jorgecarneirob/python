from termcolor import colored
print(colored(' *'*10,'Este código verifica se o número é par ou impar.',' *'*10),'red')
n = float(input('Informe um número: '))
if (n % 2) == 0:
    print('{}\nO número digitado é: {} e ele é par!\n{}'.format(' #'*20,n , ' #'*20))
else:
    print('{}\nO número digitado é {} e ele é impar!\n{}'.format(' #'*20, n, ' #'*20))
