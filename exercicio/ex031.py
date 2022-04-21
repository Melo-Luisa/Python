print('--- CALCULANDO TODA A VIAGEM ---')
viagem = float(input('Qual a distância percorrida? Km/h'))
if viagem <= 200:
    multa1 = viagem * 0.50
    print('O total de sua viagem é R$ {}'.format(multa1))
else:
    multa2 = viagem * 0.45
    print('O total de sua viagem é R$ {}'.format(multa2))
'''preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(preço))'''
print ('='* 25)
print ('Faça uma boa viagem ;)')
print ('='* 25)
#corrigido
