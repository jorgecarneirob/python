print('\033[31m* \033[m' * 40)
print('{:=^40}'.format('Este código calcula desconto de acordo com o meio de pagamento'))
print('\033[31m* \033[m' * 40)
preco = float(input('Informe o valor do produto R$: '))
meio = int(input('''Selecione o meio de pagamento:
[ 1 ] Á vista dinheiro.
[ 2 ] Á vista cartão
[ 3 ] Cartão 2x
[ 4 ] Cartão acima 3x
Informe o número do meio de pagamento: '''))

if meio == 1:
    print('''Seu pagamento será em dinheiro o produto é R$: {}
Você tem 10% de desconto R$: {}'''.format(preco, preco - preco * 0.10))

elif meio == 2:
    print('''Seu pagamento será no cartão o produto é R$: {} 
Você tem 5% de desconto R$: {}'''.format(preco, preco - preco * 0.05))

elif meio == 3:
    print('''Seu pamento será parcelado no cartão no cartão em 2x de R$: {} 
Total R$: {}'''.format(preco / 2, preco))

elif meio == 4:
    parcelas = int(input('Informe a quantidade de parcelas: '))
    print('''O produto é R$:{}
    Será parcelado em: {} de R$:{} 
    No cartão com acréscimo de 20% R$:{}'''.format(preco, parcelas, preco / parcelas, preco + preco * 0.20))

else:
    print('[ \033[31mERRO\033[m ] Meio de pagamento não encontrado.')