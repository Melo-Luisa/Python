nome = str(input('Qual é o seu nome? '))
if nome == 'Luisa':
    print('Que nome bonito!')
elif nome == 'Liliana' or nome == 'Sofia':
    print('Seu nome é bem popular na minha família')
elif nome in 'Portella Agatha Iluminado':
    print('Que belo nome feminino')

print ('Tenha um bom dia, {}!'.format(nome))
