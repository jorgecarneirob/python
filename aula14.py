print('\033[33m* \033[m' * 40)
print('Este código usa while.'.center(80))
print('\033[33m* \033[m' * 40)

n = 1
p = 0
i = 0
cont = 0

while n != 0:
    cont +=1
    n = int(input('Digite um valor ou 0 para sair: '))
    if n != 0:
        if n % 2 == 0:
            p +=1
        else:
            i +=1

print(''' Foram digitados {} valores.
{} são PAR.
{} são IMPAR.'''.format(cont, p, i))