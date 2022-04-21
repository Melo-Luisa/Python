#lista de preço com tupla
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno',  15.90, 'Estojo', 25.00, 'Trasferidor', 4.20, 'Compasso',
9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    #Contando na tupla o nomes do produto está na frente o preço atrás, sendo produto = 0(par) e preço= 1(ímpar)
    if pos % 2 == 0: #par
        #aqui mostra os (0,2,4,6,8...)
        print(f'{lista[pos]:.<30}', end='')
    else:
        #aqui mostra (1,3,5,7,9...)
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)
#corrigido