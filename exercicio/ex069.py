#cadastro de pessoas
maior = homens = mulheresmenores = 0
print('=-=' * 10)
print('     CADASTRO DE PESSOAS     ')
print('=-=' * 10)
while True: #cadastro
    idade = int(input('>> Digite a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('> Informe o sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:#maior de 18
        maior += 1
    if sexo == 'M': #homens contagem
        homens += 1
    if sexo == 'F' and idade <= 20: #mulher menor de 20 anos
        mulheresmenores += 1
    pergunta = ' '
    while pergunta not in 'YN':
        pergunta = str(input('- Você deseja cadastrar mais pessoas? [Y/N]')).strip().upper()[0]
        print('=' * 20)
    if pergunta == 'N':
        break
print(f'Número de pessoas que possuem mais de 18 anos: {maior}')
print(f'O número de homens cadastrado é de: {homens}')
print(f'O número de mulheres menores de 20 anos é de: {mulheresmenores}')
print('babou') 
