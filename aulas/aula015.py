cont = 0
while True: #continuar infinito
    print(cont, '-> ', end='')
    cont += 1
print('babou')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'a soma vale {s}')

nome = 'José'
idade = 33
s = 987.3
print(f'o nome {nome} tem {idade} anos e ganha R$ {s:.2f}.') #atualização