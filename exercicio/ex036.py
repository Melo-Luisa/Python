casa = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos o comprador pagará a casa?'))
p = (casa / anos * 12)
print('Para pagar uma casa de R$ {} em {} anos, deverá pagar de prestação R$ {:.2f}'.format(casa, anos, p))
if p >= (s * 0.3):
    print('Empréstimo negado')
else:
    print('Empréstimo deferido')
