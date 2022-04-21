from random import choice
from time import sleep
print('-=-' * 19)
print('De um número de 0 a 5, qual eu pensei?')
print('-=-' * 19)
pc = [0, 1, 2, 3, 4, 5]
escolha = choice(pc)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei no número {} e você escolheu {}!'.format(escolha, jogador))
print('--FIM--')


