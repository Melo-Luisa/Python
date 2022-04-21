#ler numeros e colocar numa lista
list = []
r = ''
while True:
    n = int(input('Digite um número:'))
    list.append(n) 
    r = str(input('Deseja continuar? [Y/N]')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'Sua lista numérica: {list}')
print(f'Sua lista contém {len(list)} números.')
list.sort(reverse=True)
print(f'Sua lista de forma decrescente é: {list}')
if 5 in list:
        print('O número 5 está na lista')
else: 
    print('Não achei o número 5')
