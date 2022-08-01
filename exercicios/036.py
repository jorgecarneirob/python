from time import sleep
cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
print(cores['vermelho'],'* '*40, cores['limpa'])
print('                          Empréstimo bancário.')
print(cores['vermelho'],'* '*40, cores['limpa'])
casa = float(input('Informe o valor da casa R$: '))
salario = float(input('Informe seu salário R$: '))
prazo = int(input('Quantidade de parcelas?: '))
resultado = casa / prazo
print(cores['amarelo'],'* '*40, cores['limpa'])
print('                                 Calulando...')
print(cores['amarelo'],'* '*40, cores['limpa'])
sleep(3)
if resultado >= salario*0.30:
    print('{}O valor da parcela é de R$: {}\nInfelizmente a parcela é muito alta!.{}'.format(cores['vermelho'], resultado, cores['limpa']))
else:
    print('{}O valor da parcela é de R$: {}\nEmpréstimo aprovado!{}'.format(cores['verde'], resultado, cores['limpa']))
