print('\033[31m* \033[m' * 40)
print('                         Calcula o IMC.')
print('\033[31m* \033[m' * 40)
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a dua altura: '))
resultado = peso / altura ** 2
if resultado < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(resultado))
elif resultado > 18.5 and resultado < 25:
    print('Seu IMC é: {:.2f} e você está no peso ideal!'.format(resultado))
elif resultado >= 25 and resultado < 30:
    print('Seu IMC é: {:.2f} e você tem sobrepeso.'.format(resultado))
elif resultado >= 30 and resultado < 40:
    print('Seu IMC é: {:.2f} e você está obeso.'.format(resultado))
else:
    print('Seus IMC é: {:.2f} e você tem obesidade morbida.'.format(resultado))