#lista de pares e ímpares
from time import sleep
princ = [[], []]
valor = 0
print('-' * 30)
print('{:^30}'.format('ANALISANDO NÚMEROS'))
print('-' * 30)
for num in range(7):
    valor = (int(input(f'Digite o {num+1}º valor:')))
    if valor % 2 == 0: #pares
        princ[0].append(valor)
    else: #impares
        princ[1].append(valor)
print('-' * 30)
princ[0].sort()
princ[1].sort
print('Analisando...')
sleep(1)
print(f'O valores pares: {princ[0]}')
print(f'O valores ímpares: {princ[1]}')
print('-' * 30)
print('\033[1;34mBy CURSO EM VIDEO\033[m')