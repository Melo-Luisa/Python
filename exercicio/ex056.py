idades_tot = 0
maioridadehomem = 0
nomevelho = 0
tot_mulher20 = 0
for compi in range(1, 4+1):
    print('----- {}ª PESSOA -----'.format(compi))
    nome = str(input('Qual o nome da pessoa?')).upper().strip()
    idade = int(input('Qual a idade da pessoa?'))
    print('''Escolha as opções de sexo:
    [ 1 ] FEMININO
    [ 2 ] MASCULINO''')
    opcao = int(input('Qual a opção da pessoa?'))
    idades_tot += idade
    if opcao == 2 and idade > maioridadehomem:
       maioridadehomem = idade
       nomevelho = nome
    if opcao == 2 and idade < 20:
        tot_mulher20 += 1
media = idades_tot / 4
print('-' * 10)
print('A média das idades no grupo é de {:2} anos.'.format(media))
print('-' * 10)
print('O homem mais vehos tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('-' * 10)
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_mulher20))
print('-' * 10)
