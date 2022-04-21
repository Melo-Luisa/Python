from datetime import date
ano = int(input('Informe a sua data de nascimento:'))
alistamento = date.today().year - ano
if alistamento > 18:
    m = (alistamento - 18)
    print('Você tem {} de idade e já deveria ter se alistado à {} anos atrás'.format(alistamento, m))
    ada = date.today().year - m
    print('Seu alistamento foi em {}'.format(ada))
elif alistamento < 18:
    m2 = (18 - alistamento)
    print('Você tem {} de idade e ainda não está na hora de se alistar! Falta {} anos'.format(alistamento, m2))
    adl = date.today().year + m2
    print('Seu alistamento será em {}'.format(adl))
else:
    print('Você está na idade do alistamento')

