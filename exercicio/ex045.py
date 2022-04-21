from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=' * 15)
print('O computador jogou {}'.format(itens[computador]))
print('A sua jogada foi {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: #pedra
    if jogador == 0:
        print('\033[34mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[7;31mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[1;4;31mJOGADA INVÁLIDA\033[m')
elif computador == 1: #papel
    if jogador == 0:
        print('\033[7;31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCE\033[m')
    else:
        print('\033[1;4;31mJOGADA INVÁLIDA\033[m')

elif computador == 2: #tesoura
    if jogador == 0:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[7;31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE\033[m')
    else:
        print('\033[1;4;31mJOGADA INVÁLIDA\033[m')
#corrigido