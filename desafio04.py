from xmlrpc.client import Boolean, boolean

print('Desafio identificando typo de input.')
n = (input('Digite algo: '))
a = (type(n))
b = boolean((n.isalnum()))
c = boolean((n.isnumeric()))
print('O input foi: {} é do tipo {} Alphanumerico? {} Numerico? {}'.format(n, a, b, c))
