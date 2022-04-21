#números aleatorios em tupla e dizer o maior e menor
from random import sample
random_numbers = sample(range(10), 5)#fazer a lista de até 10 números mostrando apenas 5 deles
print('=-' * 15)
print(f'A lista do números foi: ', end='')
for n in random_numbers:
    print(f'{n} ', end='')
print(f'\n>> O maior valor sorteado foi {max(random_numbers)}')
print(f'> O menor valor sorteado foi {min(random_numbers)}')
print('Babou')
print('=-' * 15)
#corrigido de um modo diferente porém correto