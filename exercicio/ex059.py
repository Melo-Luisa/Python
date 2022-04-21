from time import sleep
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
opcao = 0
while opcao != 5:
    print('''Escolha a forma de equação dos números:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>>> Informe a sua opção:'))
    if opcao == 1:
        print('A soma entre os valores {} e {} é igual a {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação dos valores {} e {} é igual a {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print('Entre os valores {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção inválida!! Tente novamente.')
    print('=-=' * 10)
    sleep(1.5)
print('Fim do programa! Volte sempre!')    