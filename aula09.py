from datetime import datetime


frase = "  Curso em video de python  "
print('Fatia uma string dentro da variável: {}'.format(frase[2::2]))
print('Exibe a quantidade de caracteres dentro da variável: {}'.format(len(frase)))
print('Procura um trexo dentro da variável: {}'.format( frase.find('de')))
print('Altera uma informação dentro da variável: {}'.format(frase.replace('python', 'android')))
print('Deixa tudo em maiusculo: {}'.format(frase.upper()))
print('Deixa tudo em minusculo: {}'.format(frase.lower()))
print('Capitaliza a frase: {}'.format(frase.capitalize()))
print('Maiusculas em todas as palavras: {}'.format(frase.title()))
print('Frase sem strip: {} frase com strip: {}'.format(frase, frase.strip()))
print('Frase sem strip: {} frase com Rstrip: {}'.format(frase, frase.rstrip()))
print('Frase sem strip: {} frase com Lstrip: {}'.format(frase, frase.lstrip()))