#ATM 
print('{:=^40}'.format('BANKINHO'))
print('A Máquina só possui cédulas de: R$ 50, R$ 20, R$ 10 e R$ 1.')
valor = int(input('> Qual será o valor a ser sacado: R$'))
total = valor
ced = 50 #mair valor na máquina
totced = 0
while True:
    if total >= ced: #se o valor a sacar for maior q 50 conto
        total -= ced #então tira 50
        totced += 1 #adicionando 1 ao total
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}.')
        if ced == 50: #para substituir as cédulas por outras até R$ 1
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0: #sair do pragrama pois não há mais como dividir para entregar as cédulas 
            break
print('-' * 30)
print('Não tenha uma bom dia, tenha um ótimo dia.')
print('Babou.')
#corrigido