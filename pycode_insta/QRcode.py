import pyqrcode
import png
from pyqrcode import QRCode

QRString = input('Digite o link: ')
arq = input('Informe o nome do arquivo com extensão: ')
url = pyqrcode.create(QRString)
url.png(arq, scale=8)