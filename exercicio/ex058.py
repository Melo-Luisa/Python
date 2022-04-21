from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qua foi?')
acertou = False #primeira opção negativa
palpites = 0 #para somar mais tarde nas tentativas
while not acertou: #negativo 
    jogador = int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:#caso contrario de não acerto fazer as novas tentativas de mais ou menos
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou!! Com {} tetativas. Parabéns!!'.format(palpites))#sai do True e vem para o acerto
#corrigido