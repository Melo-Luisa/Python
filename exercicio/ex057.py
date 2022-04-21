#Coloca F e M no while como opção de sexo
nome = str(input('Informe o seu nome:')).strip().upper()
sexo = str(input('Informe o seu sexo: [F/M/NB]')).strip().upper()[:2]#fatiamento para pegar o primeiro num
while sexo not in 'MFNB':
    sexo = str(input('Dados Inválidos. Por favor, informe se sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
print('Tenha um bom dia, {}!'.format(nome))
#While pode ser colocado com negativos
#corrigido