from math import factorial
print('=-=' * 15)
print('    RESOLVENDO UM FATORIAL    ')
print('=-=' * 15)
n = int(input('Informe um número:'))
c = n
f = 1
print('Calculando {}! ='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
#corrigido