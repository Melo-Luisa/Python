#ler numeros e colocar em lista em ordem e sem duplicações
listanum = []
while True:
    numeros = int(input('Digite um número:'))
    #se os numeros digitados não estiverem na lista será adicionado
    if numeros not in listanum:
        listanum.append(numeros)
        print('Valor Adicionado...')
    #caso contrário, não
    else:
        print('Valor já adicionado...Não será contado.')
    #não conseguir add o while para apenas receber respostas de 'YN'
    pergunta = str(input('Você deseja continuar? [Y/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
#primeiro coloca em ordem dps manda mostrar
listanum.sort()
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print('\nbabou')
#corrigido