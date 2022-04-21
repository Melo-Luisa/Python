#ler número diferentes de 999
num = -1
cont = -999
total = -1
while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    cont += num 
    total += 1 
print ('Você digitou {} números e a soma entre eles foi {}.'.format(total, cont))
print('FIM.')
#voltar na aula 15 porém corrigido