print('\033[31m* \033[m' * 40)
print('             Este código recebe 6 números e soma os pares.')
print('\033[31m* \033[m' * 40)
for x in range (0, 6):
    n = int(input('Digite um número inteiro: '))
    soma = 0
    if (n % 2) == 0:
        soma = n+n
print(soma)