from datetime import date 
cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}
print(cores['vermelho'],'* '*40, cores['limpa'])
print('                          Verifica se precisa se alistar.')
print(cores['vermelho'],'* '*40, cores['limpa'])
nasc = int(input('Informa o ano de nascimento: '))
idade = date.today().year - nasc
sexo = str(input('Informe M para Masculino e F para Feminino: ')).upper()
if idade < 18 and sexo == 'M':
    print('Sua idade é: {}\nFaltam: {} anos para você se alistar'.format(idade, 18 - idade))
elif idade > 18 and sexo == 'M':
    print('Sua idade é: {} e você já passou {} anos para se alistar'.format(idade, idade - 18))
elif idade == 18 and sexo == 'M':
    print('Sua idade é 18 e você deve se alistar este ano!')
else:
    print('Você é do sexo feminino e mulheres não precisam se alistar.')

