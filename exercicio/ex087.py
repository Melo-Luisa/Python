#matriz em python 2.0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
#l = linha
for l in range(3):
    #c = coluna
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]:'))
print('=' * 30)
#for de estrutura
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:#par
            spar += matriz[l][c]
    print()
print('-' * 25)
print(f'A soma das coordenadas pares são: {spar}')
for l in range (3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior número da segunda linha é: {mai}')
print('\n\033[1;34mBy CURSO EM VIDEO\033[m')
#corrigido