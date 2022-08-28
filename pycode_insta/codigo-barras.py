#autor: Jorge Carneiro
#email:jorgecarneirob@hotmail.com

from barcode import EAN13
from barcode.writer import ImageWriter
print('\033[31m* \033[m' * 50)
print('''Este código gera codigos de barras.'''.center(100))
print('\033[31m* \033[m' * 50)
codigo = input('Informe o EAN: ')
with open(r'C:\Users\Fer Lima\Documents\GitHub\python\codbarras.png','wb') as f:
    EAN13(codigo, writer=ImageWriter()).write(f)