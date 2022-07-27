import playsound
print('Este código toca um arquivo de audio.')
c = input('Informe o caminho do arquivo: ')
print('Tocando o arquivo: {}'.format(c))
playsound.playsound(c)