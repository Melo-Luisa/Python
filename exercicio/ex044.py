print('-' * 20)
print('\033[35mFORMAS DE PAGAMENTO\033[m')
print('-' * 20)
preço = float(input('Informe o valor da compra: R$'))
print(''''Informe a forma de pagamento:
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual será a forma de pagamento? '))
if opcao == 1:
    desconto1 = preço - (0.1 * preço)
    print('\033[32mPARABÉNS\033[m! A sua compra deu um desconto de 10%! A sua compra era de R$ {} e ficou em R$ {}. Efetue o seu pagamento no caixa.'.format(preço, desconto1))
elif opcao == 2:
    desconto2 = preço - (0.05 * preço)
    print('\033[32mPARABÉNS\033[m! A sua compra deu um desconto de 5%! A sua compra era de R$ {} e ficou em R$ {}. Efetue o seu pagamento no caixa.'.format(preço, desconto2))
elif opcao == 3:
    parcela = preço / 2
    print('A sua compra custa R$ {} e será feita em 2 parcelas de {}. SEM JUROS. Efetue o pagamento no caixa. E Fique atento as nossas promoções!'.format(preço, parcela))
elif opcao == 4:
    perguntar = int(input('Em quantas parcelas deseja fazer a compra?'))
    juros = (preço * 0.2)
    valorfinal = preço + juros
    mes = preço / perguntar
    print('A sua compra foi de R$ {} e será feita em {} parcelas de R$ {:.2f}, e terá um juros de {:.2f}, o que totalizará em R$ {}.'.format(preço, perguntar, mes, juros, valorfinal))
else:
    print('\033[4;31mERROR\033[m')