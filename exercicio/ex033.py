from random import choice
num1 = int(input('informe 1º números:'))
num2 = int(input('informe o 2º número:'))
num3 = int(input('informe o 3º número:'))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 > num1 or num3 > num2:
    menor = num3
#Verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor valor digitado é {}'.format(menor))
print('O maior valaor digitado é {}'.format(maior))
#corrigido
