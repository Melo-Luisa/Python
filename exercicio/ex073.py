#Brasileirão serie A - 2021
lista = ('ATLÉTICO-MG', 'FLAMENGO', 'PALMEIRAS', 'FORTALEZA', 'CORINTHIANS', 'BRAGANTINO', 
'FLUMINENSE', 'AMÉRICA-MG', 'ATLÉTICO-GO', 'SANTOS', 'SANTOS', 'CEARÁ SC', 'INTERNACIONAL', 
'SÃO PAULO', 'ATHETICO-PR', 'CUIABÁ', 'JUVENTUDE', 'GRÊMIO', 'BAHIA', 'SPORT RECIFE', 'CHAPECOENSE')

print('-' * 60)
print(f'Os times do Brasileirão são: {lista}')
print('-=' * 15)
print(f'>>>> Os primeiros 5 da lista do Brasileirão de 2021 são: {lista[:5]} ')
print('-=' * 15)
print(f'>>> Os últimos colocado na lista do Brasileirão de 2021 são: {lista[-4:]}')
print('-=' * 15)
print('>> A lista do Braisleirão em ordem alfabética:')
print(sorted(lista))
print('-=' * 15)
print(f'O Chapecoense está na {lista.index("CHAPECOENSE")}º posição')
print('-' * 60)
#corrigido
