print('-=' * 10)
print('\033[31m      TABUADA      \033[m')
print('-=' * 10)
num = int(input('Digite um número para ver sua tabuada:'))
for n in range(1, 11):
    t = num * n
    print('{} x {} = {}'.format(num, n, t))
'#corrigida'
