print('\033[31m* \033[m' * 40)
print('''            Este código exibe a somente de todos os numeros 
                 impares multiplos de 3 de 1 até 500''')
print('\033[31m* \033[m' * 40)
soma = 0
contador = 0
for c in range(0,501):
    if (c % 2) == 1 and c % 3 == 0:
        soma += c
        contador += 1
        print(c)
print('A soma de todos os {} valores é: {}'.format(contador,soma))
