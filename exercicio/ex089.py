#boletim
original = []
print('-' * 30)
print('{:^30}'.format('BOLETIM ESCOLAR'))
print('-' * 30)
while True:
    nome = (str(input('Digite o nome do aluno(a):')))
    nota1 = (int(input(f'Digite a 1º nota:')))
    nota2 = (int(input(f'Digite a 2º nota:')))
    media = (nota1 + nota2)/2
    #lista
    original.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [Y/N]')).strip().upper()[0]
    if resp == 'N':
        break
    print('-' * 30)
print('-=' * 25)
print('{:^30}'. format('NOTAS'))
print('-=' * 25)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(original):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(original) - 1:
        print(f'Notas de {original[opc][0]} são {original[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
