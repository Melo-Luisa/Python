# ler pessoas e peso e depois responder as questões
pessoas = []
nome = []
cadas = mais = menos = 0
while True:
    print('-' * 25)
    print('{:^25}'.format('CADASTROS E PESOS'))
    print('-' * 25)
    nome.append(str(input('Digite o seu nome: ')))
    nome.append(int(input('Digite o seu peso: ')))
    if len(pessoas) == 0:
        mais = menos = nome[1]
    else:
        if nome[1] > mais:
            mais = nome[1]
        if nome[1] < menos:
            menos = nome[1]        
    #copia
    pessoas.append(nome[:])
    #limpar a lista para n repetir
    nome.clear()
    r = str(input('Deseja continuar? [Y/N]')).strip().upper()[0]
    if r == 'N':
        break
for i in pessoas:
    cadas += 1
print(f'Total de pessoas cadastradas: {cadas}') #ou len(pessoas)
print(f'O maior peso foi {mais}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mais:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {menos}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menos:
        print(f'{p[0]} ', end='')
print()
print('-=' * 30)
print('\033[1;32mby CURSO EM VIDEO\033[m')