soma = 0
con = 0
for c in range(1, 7):
   num = int(input('Digite o primeiro número:'.format(c)))
   if num % 2 == 0:
        soma += num
        con+= +1
print('Você informou {} números e a soma foi {}'.format(con, soma))
'#corrigido'
