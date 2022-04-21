#ler uma expressão numérica e analisar os parenteses
#toda str é uma lista
expr = str(input('Digite a expressão:'))
pilha = []
#s = símbolo
for s in expr:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expresão esta válida!')
else:
    print('Sua expresão está inválida!')
#corrigido
