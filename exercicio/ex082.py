lista1 = []
pares = []
impar = []
while True:
    lista1.append(int(input('Digite um valor:')))
    r = str(input('Deseja continuar? [Y/N]')).strip().upper()[0]
    if r in 'N':
        break
for i, v in enumerate(lista1):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v) 
print('-=' * 30)
print(f'Sua lista: {lista1}')
print(f'Sua lista apenas com números pares: {pares}')
print(f'Sua lista com apenas números ímpares: {impar}')