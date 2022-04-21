# lendo pesos, qual o maior e qual o menor
tot_maior = 0
menor = 0
for p in range(1, 5+1):
    peso = float(input('Qual é o {}º peso?'.format(p)))
    if p == 1:
        tot_maior = peso
        menor = peso
    else:
        if peso > tot_maior:
            tot_maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg'.format(tot_maior))
print('O menor peso é {}Kg'.format(menor))
#corrigido
