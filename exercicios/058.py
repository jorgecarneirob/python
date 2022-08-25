from random import randint
print('\033[31m* \033[m' * 50)
print('''Este código faz um sorteio.'''.center(100))
print('\033[31m* \033[m' * 50)
valido = False
tentativas = 0
while not valido:
    pc = randint(0,3)
    user = int(input('Digite um número entre 0 - 3: '))
    if pc == user:
        print('''O valor sorteado foi {}.
você digitou {}
Você tentou {}x para acertar!
'''.format(pc, user, tentativas))
        valido = True
    else:
        print('''O valor sorteado foi {}.
você digitou {}
TENTE NOVAMENTE.
=================================='''.format(pc, user))
        tentativas +=1