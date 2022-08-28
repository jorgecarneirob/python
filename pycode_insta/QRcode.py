#autor: Jorge Carneiro
#email:jorgecarneirob@hotmail.com

import pyqrcode
import png
from pyqrcode import QRCode
print('\033[31m* \033[m' * 50)
print('''Este código gera QRCode de um link.'''.center(100))
print('\033[31m* \033[m' * 50)
QRString = input('Digite o link: ')
arq = input('Informe o nome do arquivo com extensão: ')
url = pyqrcode.create(QRString)
url.png(arq, scale=8)
