print('\033[31m* \033[m' * 40)
print('                     Este programa confere um palindromo.')
print('\033[31m* \033[m' * 40)
f = input('Digite a frase: ')
i = f.upper().strip().replace(' ', '')
x = i[::-1]
p = f[::-1]
if i == x:
    print('A frase digitada foi: {}\nO inverso é palindromo: {}'.format(f,p))
else:
    print('A frase digitada foi: {}\nO inverso NÃO é palindromo: {}'.format(f,p))
