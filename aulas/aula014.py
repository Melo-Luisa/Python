#TESTES DA AULA 014 - MUNDO 02
for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')


#condição de parada
r = 'Y'
while r == 'Y':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [Y/N]')).upper()
print('FIM')


#leve gambirra
n = 1 #para não pegar no while como diferente de 0
par = impar = 0 #igualar os números
while n != 0: #enquanto o n for diferente de 0 irá fazer os if's
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0: #par
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
