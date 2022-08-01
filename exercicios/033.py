print (' *'*20, 'Este código retorna o maior e o menor de 3.',' *'*20)
v1 = float(input('Informe o 1° valor: '))
v2 = float(input('Informe o 2° valor: '))
v3 = float(input('Informe o 3° valor: '))
maior = v1
menor = v1

#verifica maior
if v2>v1 and v2>v3:
    maior = v2
if v3>v1 and v3>v1:
    maior = v3

#verifica menor
if v2<v1 and v2<v3:
    menor = v2
if v3<v1 and v3<v2:
    menor = v3
print('{}\n\033[33mOs valores são: {}, {}, {} respectivamente.\n\033[31mO maior é: {} \033[32me o menor é: {}\n{}'
.format(' #'*25,v1, v2, v3, maior, menor,' #'*25))