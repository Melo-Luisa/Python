soma = 0
cont = 0
for a in range (1, 501, 2):
    if a % 3 == 0:
        cont += 1
        soma += a
print('A soma de todos os {} valores solicitados é {}'. format(cont, soma))

