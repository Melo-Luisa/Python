#mostra os números por extenso+
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'deznove', 'vinte')
pergunta = ''
num = 0
while 0 <= num <= 20:
    num = int(input('Digite o seu número:'))
    print(f'Você digitou {cont[num]}')
    pergunta = str(input('Você deseja continuar? [Y/N]')).strip().upper()[0]
    if pergunta in 'N':
        break
print('Babou')
#CONSEGUI PORRA