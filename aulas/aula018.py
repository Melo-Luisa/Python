#Lista | parte 02
#TEORIA
#variáveis composta
#dados = ['pedro', 25]
#pessoas = [['pedro', 25],['maria', 19], ['joao', 32]]
#             0       1     0       1       0     1
#                  0            1              2
#pessoas.append(dados[:])
#print(pessoas[0][0])#pedro
#print(pessoas[1][1])#19
#print(pessoas[2][0])#joao
#print(pessoas[1])#['maria', 19]

#PRÁTICA
#galera = [['joao', 19],['ana', 33],['joaquim', 13],['maria', 45]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')
galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1 

print(f'Temos {totmai} maiores e {totmen} menores de idade ')