#cadastro de produtos de supermercado
produtos = total = menor = cont = barato = 0
while True:
    print('=' * 22)
    print(' CADASTRO DE PRODUTOS')
    print('=' * 22)
    nome = str(input('Nome do produto:'))
    preco = float(input('Preço do produto: R$'))
    cont += 1
    continuar = ' '
    while continuar not in 'YN':
        continuar = str(input('Você deseja continuar: [Y/N]')).strip().upper()[0]
        total += preco#somando a compra
        if preco >= 1000:#preço maior que R$1.000
            produtos += 1

        if cont == 1 or preco < menor:
            menor = preco #dizer que é o menor
            barato = nome
    if continuar == 'N':#sair
        break
print('{:-^40}'.format('ÁNALISE'))#formatar e centralizar
print(f'>>> Você comprou R${total:.2f} em produtos.')   
print(f'>> Número de produtos que custam mais de R$ 1.000,00: {produtos}')  
print(f'> O produto com o menor preço custa: R$ {menor} e foi {barato}.')   
print('babou')
#corrigido