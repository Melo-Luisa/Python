nome = str(input('Qual o seu nome?'))
cor = {'ciano':'\033[4;36m',
       'limpa':'\033[m'}
print('É um prazer te conhecer, {}{}{} !'.format(cor['ciano'], nome, cor['limpa']))
