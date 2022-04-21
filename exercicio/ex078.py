numeros = []
maior = menor = 0
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um número posisção {cont}:')))
    if cont == 0:#primiero valor sendo maior e menor
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]
print('-' * 30)
print(f'Você digitou os números: {numeros}')
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()
print('-' * 30)
#corrigido