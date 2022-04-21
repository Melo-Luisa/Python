#jogo par e impar - máquina x jogador
from random import randint
print('=' * 20)
print('JOGO: PAR OU ÍMPAR')
print('=' * 20)
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end= '')
    print('\033[1;32mDEU PAR\033[m' if total % 2 == 0 else "\033[1;31mDEU ÍMPAR\033[m")
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
    elif tipo == 'I':
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
    print('=' * 20)
print(f'GAME OVER! Você venceu {v} vezes')
print('=' * 30)
#tem algo de errado