print('Este cópdigo exibe algumas possibilidades sobre manipulação de texto.')
frase = "   Curso em Video de python   "
print('Fatia uma string dentro da variável: {}'.format(frase[0:6]))
print('Exibe a quantidade de caracteres dentro da variável: {}'.format(len(frase.strip().split())))
print('Conta uma letra ou texto dentro da variável: {}'.format(frase.count('o')))
print('Procura um trexo dentro da variável: {}'.format( frase.find('de')))
print('Altera uma informação dentro da variável: {}'.format(frase.replace('python', 'android')))
print('Deixa tudo em maiusculo: {}'.format(frase.upper()))
print('Deixa tudo em minusculo: {}'.format(frase.lower()))
print('Capitaliza a frase: {}'.format(frase.capitalize()))
print('Maiusculas em todas as palavras: {}'.format(frase.title()))
print('Frase sem strip: {} frase com strip: {}'.format(frase, frase.strip()))
print('Frase sem strip: {} frase com Rstrip: {}'.format(frase, frase.rstrip()))
print('Frase sem strip: {} frase com Lstrip: {}'.format(frase, frase.lstrip()))
print('Teste de split: {}'.format(frase.split()))
frase = frase.split()
print('Teste de join: {}'.format('-'.join(frase)))
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().""")
#procura = input('O que deseja procurar na frase?:')
#print('O valor digitado é {} e {} na frase'.format(procura, procura in frase))