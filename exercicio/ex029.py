velocidade = float(input('Qual a sua velocidade em Km/h?'))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print('Você ultrapassou o limite de velocidade que era 80Km/h e sua velocidade era {}'.format(velocidade))
    print('Sua multa foi de R$ {:.2f}'.format(multa))
else:
    print('Você está na velocidade permitida!')
print('Tenha um bom dia! Dirija com segurança :)')
#corrigido