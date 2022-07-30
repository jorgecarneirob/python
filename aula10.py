print('Este programa reage ao ano de produção do carro: ')
ano = int(input('Qual ano de fabricação do seu carro? '))
#if ano <=2010:
#    print('Carro velho!')
#else:
#    print('Carro novo.')
print('Carro velho' if ano <=2010 else 'carro novo')