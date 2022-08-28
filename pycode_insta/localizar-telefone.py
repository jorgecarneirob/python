#autor: Jorge Carneiro
#email:jorgecarneirob@hotmail.com

import phonenumbers
from phonenumbers import geocoder, carrier
print('\033[31m* \033[m' * 50)
print('''Este código gera retorna operadora + localizaçao.'''.center(100))
print('\033[31m* \033[m' * 50)
# Digite seu número com codigo do país e ddd #
fone = input('Digite seu número com codigo do país e ddd: ')
phoneNumer = phonenumbers.parse(fone)
# Captura operadora #
Carrier = carrier.name_for_number(phoneNumer, 'pt-br')
# Captura região #
Region = geocoder.description_for_number(phoneNumer, 'pt-br')
# Mostra resultados #
print("A operadora é: " + Carrier)
print("O estado é: " + Region)