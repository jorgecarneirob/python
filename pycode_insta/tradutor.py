#autor: Jorge Carneiro
#email:jorgecarneirob@hotmail.com

from translate import Translator
from time import sleep
print('\033[31m* \033[m' * 50)
print('Este é um tradutor.'.center(100))
print('\033[31m* \033[m' * 50)
i = 0
while i != 3:
    i = int(input('''
Informe o idioma origem e destino:
[ 1 ] pt-br
[ 2 ] Inglês
[ 3 ] SAIR
Digite a opção: '''))
    if i == 1: 
        s = Translator(from_lang='pt-br', to_lang='english')
        t = str(input('\nInforme o texto: \n'))
        t = s.translate(t)
        print('\nTradução: \n{}'.format(t))
    elif i == 2: 
        s = Translator(from_lang='english', to_lang='pt-br')
        t = str(input('\nInforme o texto: \n'))
        t = s.translate(t)
        print('\nTradução: \n{}'.format(t))

print('Saindo')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')