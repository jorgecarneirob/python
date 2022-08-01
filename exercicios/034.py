from termcolor import colored
print(colored('* '*40,'red'), 
colored('\nEste codigo calcula a quantidade de aumento por salario.\n','green'),
colored('* '*40,'red'), )
s = float(input('Informe o salário atual R$: '))

if s >= 1250:
    n = s * 0.10 + s
else:
    n = s * 0.15 + s

print('{}{}\nO salário atual é R$: {} com aumento R$: {}\n{}').format('\033[0;31m','# '*26,s, n, '# '*26)