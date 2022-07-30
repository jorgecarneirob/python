print('Este código confere se a cidade começa com a palavra SANTO')
c = str(input('Digite no nome da sua cidade: ').strip())
print(c[:5].upper() == 'SANTO')