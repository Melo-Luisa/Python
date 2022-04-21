#matriz em python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    print()
print('\n\033[1;34mBy CURSO EM VIDEO\033[m')