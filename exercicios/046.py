from time import sleep
print('\033[31m* \033[m' * 40)
print('                         Este código faz uma contagem regressiva')
print('\033[31m* \033[m' * 40)
for c in range(10, 0, -1):
    print(c,'...')
    sleep(1)
print('\033[33mFeliz Ano NOVO!\033[m')