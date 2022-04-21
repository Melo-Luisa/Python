"""ano de nascimento de 7 pessoas, qnts maior idade e qnts não"""
from datetime import date
atual = date.today().year
tot_maior = 0
tot_menor = 0
for y in range(1, 8):
    nasc = int(input('Qual ano nasceu a {}º pessoa?'.format(y)))
    idade = atual - nasc
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(tot_maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(tot_menor))
