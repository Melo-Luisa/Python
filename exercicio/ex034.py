s = float(input('Informe o salário do funcionário: R$'))
if s >= 1250:
    a = ((s * 0.10) + s)
    print('O atual salário é R$ {:.2f}'.format(a))
else:
    a1 = ((s * 0.15) + s)
    print('O atual salário será de R$ {:.2f}'.format(a1))