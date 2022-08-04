from random import randint, choice
from time import sleep
print('\033[33m* \033[m' * 40)
print('                                 JOKENPÔ!....')
print('\033[33m* \033[m' * 40)
jogo = {'1':'PEDRA', '2':'PAPEL', '3':'TESOURA'}
user = int(input('1. PEDRA \n2. PAPEL \n3. TESOURA\nInforme o número da arma: '))
if user < 1 or user > 3:
    print('[ \033[31mERRO\033[m ] OPÇÃO INVÁLIDA.')
    exit()
pc = randint(1, 3)
print('JO...')
sleep(2)
print('KEN...')
sleep(2)
print('''PÔ!
Computador: {}
Você: {}'''.format(jogo['{}'.format(pc)], jogo['{}'.format(user)]))
if user == 1 and pc == 2 or user == 2 and pc == 1:
    print('PAPEL VENCE!')
elif user == 2 and pc == 3 or user == 3 and pc == 2:
    print('TESOURA VENCE!')
elif user == 3 and pc == 1 or user == 1 and pc == 3:
    print('PEDRA VENCE!')
elif user == pc:
    print('EMPATE!')
else:
    print('[ \033[31mERRO\033[m ]')