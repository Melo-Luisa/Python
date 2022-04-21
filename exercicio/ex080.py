#ler 5 valores (usuário) e organizar sem o sort()
valores = list()
for cont in range(6):
    numero = (int(input('Digite o número:')))
    if cont == 0 or numero > valores[-1]:
        valores.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-' * 30)
print(f'Os valores foram: {valores}')
