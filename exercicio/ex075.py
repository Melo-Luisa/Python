#ler 4 valores e responder as questões
print('=-' * 15)
n1 = (int(input('Digite o 1º número:')),
int(input('Digite o 2º número:')),
int(input('Digite o 3º número:')),
int(input('Digite o 4º número:')))
tupla = (n1)
print(f'Você digitou os números: {tupla}')
print(f'O número 9 apareceu: {tupla.count(9)} vezes.')
if 3 in n1:
    print(f'O número 3 está na posição: {tupla.index(3)+1}º.')#no index números não precisam de " ", apenas "texto"
else:
    print('O valor 2 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram', end='')
for n in n1:
    if n %2 == 0:#se par, aparece
        print(n1,  end='')
#corrigido