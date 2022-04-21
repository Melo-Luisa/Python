#\033[0;33;44m
#\033[0;30;41m - vermelho com texto em branco
#\033[4;33;44m - sublinhado azul com texto amarelo
# \033[1;35;43m - negrito amarelo com texto roxo
# \033[30;42m - verde com texto branco
# \033[m - fundo preto letra cinza
# \033[7;30m - negativo com letra branco (inversão)

print('\033[7;35;40m Olá, Mundo!\033[m')
c = 7
d = 10
print('O valor da comanda é de \033[34m{}\033[m e o valor em conta é \033[31m{}'.format(d, c))
n = 'Luisa Melo'
cores = {'Limpa' : '\033[m' , 'azul': '\033[34m' , 'amarelo': '\033[33m' , 'pretoebranco' : '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format( cores['amarelo'], n, cores['Limpa']))#ultima chave não e necessário
