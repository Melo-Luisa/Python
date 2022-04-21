#4 jogadores e o maior valor ganha
from random import randint
from time import sleep
from operator import itemgetter
info = {
    'jogador1': randint(1,6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1 ,6)
}
ranking = {}
print('Valores sorteados: ')
for k, v in info.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
#ordem
ranking = sorted(info.items(), key=itemgetter(1), reverse=True)
print('-' * 30)
print('{:^30}'.format('RANKING'))
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
