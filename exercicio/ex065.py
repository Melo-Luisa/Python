#rodar uns números, depois mostrar numeros qnts, medias, maior e menor
r = 'Y'
soma = quant = media = maior = menor = 0
while r == 'Y':
    num = int(input('>>Digite um número:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('>Você deseja continuar? [Y/N]')).strip().upper()[0] 
media = soma / quant
print('Você digitou {} números e a média dos números é {:.2f} .'.format(quant, media))
print('O maior valor foi {} e o menor {}.'.format(maior, menor))
print('babou!')
#corrigido