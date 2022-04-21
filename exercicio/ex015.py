print('CARRO ALUGADO - GASTOS')
c = float(input('Informe a placa do carro: '))
km = float(input('Informe quantos km o carro andou:'))
d = int(input('Informe quantos dias:'))
p = ((60 * d) + (0.15 * km))
print('O consumo do carro {} foi de R$ {:.2f}'. format(c, p))
#corrigido
