#autor: Jorge Carneiro
#email: jorgecarneirob@hotmail.com

import pyshorteners
print('\033[31m* \033[m' * 50)
print('''Este código gera URL encurtada.'''.center(100))
print('\033[31m* \033[m' * 50)
url = input('Informe a URL: ')
#Carrega lib
s = pyshorteners.Shortener()
#Gera URL
shortUrl = s.tinyurl.short(url)
#Exibe resultado
print(f'URL curta: {shortUrl}')