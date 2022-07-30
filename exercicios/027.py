print('Este exercício é sobre manipulação de textos: ')
nome = input('Digite seu nome completo: ').strip()
fatiado = nome.split()
print('Primeiro nome é: {}\nSegundo nome é: {}'.format(fatiado[0], fatiado[len(fatiado)-1]))