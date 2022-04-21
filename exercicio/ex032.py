from datetime import date
print('ESSE ANO É BISSEXTO?')
ano = int(input('Me informe o ano ou coloque 0 para informar o ano atual: '))
b = ano % 4
if ano == 0:
    ano = date.today().year
if b == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
#corrigido
