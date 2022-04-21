#Ler os 'aeiou' de uma tuplas
palavras = ('OLHAR', 'MESA', 'PAREDE', 'PANELA', 'CARRO', 'PLANTA', 'LIVRO', 'SACOLA', 'ESPACO', 'ESTRELA',
'CAIXA', 'CORACAO', 'OCULOS', 'DOUTOR', 'ENGENHEIRO', 'TECNOLOGIA', 'ANEL')
ordem = (sorted(palavras))
print('-' * 30)
print('VOGAIS NAS PALAVRAS')
print('-' * 30)
for lista in ordem:
    print(f'\n{lista} com tem:', end='')
    for letra in lista:
        if letra.lower() in 'aeiou':
            print (letra, end=' ')
#corrigido