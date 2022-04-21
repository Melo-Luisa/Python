print('=' * 35)
print('Usando o FLAG [999] o programa para')
print('=' * 35)
n = s = s1 = 0
while True: #loop infinito
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break #para parar
    s += 1
    s1 += n
print(f'Você digitou {s} vezes.', end=' ')
print(f'A soma do números digitados foi {s1}.')
print('Babou!')
#corrigido
