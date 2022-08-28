#autor: Jorge Carneiro
#email:jorgecarneirob@hotmail.com

from barcode import EAN13
from barcode.writer import ImageWriter
codigo = input('Informe o EAN: ')
with open(r'C:\Users\Fer Lima\Documents\GitHub\python\codbarras.png','wb') as f:
    EAN13(codigo, writer=ImageWriter()).write(f)