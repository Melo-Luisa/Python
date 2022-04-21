print('DESCONTO!!')
p = float(input('Qual o preço do produto? R$'))
d = p - (p * 5/100)
print('O valor é {:.2f} e ficará por R$ {:.2f}'.format(p,d))
#corrigido