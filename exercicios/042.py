print('* '*40), 
print('Este código verifica se é possível montar um triangulo.'),
print('* '*40)
a = float(input('Informe o 1° valor: '))
b = float(input('Informe o 2° valor: '))
c = float(input('Informe o 3° valor: '))

if a < b + c and b < a + c and c < a + b:
    print('ESTES VALORES FORMAM UM TRIANGULO!')
    if a == b == c:
        print('{}, {}, {} FORMAM UM TRIANGULO EQUILÁTERO.'.format(a, b, c))
    if a != b != c != a:
        print('{}, {}, {} FORMAM UM TRIANGULO ESCALENO.'.format(a, b, c))
    else:
        print('{}, {}, {} FORMAR UM TRIÂNGULO ISÓSCELES'.format(a, b, c))
else:
    print('ESTE VALORES NÃO FORMAM UM TRIANGULO')