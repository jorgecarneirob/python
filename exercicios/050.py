print('\033[31m* \033[m' * 40)
print('             Este código recebe 6 números e soma os pares.')
print('\033[31m* \033[m' * 40)
soma = 0
cont = 0
for x in range (0, 6):
    n = int(input('Digite um número inteiro: '))
    if (n % 2) == 0:
        soma += n
        cont += 1
print('Você digitou {} numeros pares e a soma deles é: {}'.format(cont,soma))