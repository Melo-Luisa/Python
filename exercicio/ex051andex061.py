#P.A
print('-' * 27)
print('  GERENCIADOR DE P.A 2.0  ')
print('-' * 27)
termo = int(input('>> Digite o primeiro termo da P.A:'))
razao = int(input('> Digite a razão:'))
var = 0
while var < 10: 
    p_a = termo + var * razao
    var += 1 #somar na conta e não ser infinito
    print(p_a, end=' - ' if var < 10 else '. ') 
print('\nFIM', end=' ')

'''for var in range(0, 10):
    p_a = termo + var * razao
    print(p_a, end=' - ')''' 