print('Este código procura o nome SILVA')
n = input('Digite o nome: ').strip().upper()
s =  n.split()
print('O nome digitado é: {} e {} contém o nome SILVA'.format(n, 'SILVA' in s))