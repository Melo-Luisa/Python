#aula 16 | Tuplas
lanche = ('Hamburguer','Suco','Pizza','Pudim', 'Batata Frita')
print(f'Eu vou comer {lanche[1]}')#suco
print(sorted(lanche))#mostra o lanche em ordem alfabetica
#sem posição - tradiconal
for comida in lanche:
    print(f'Eu vou comer {comida}')#lista de todos

for cont in range (0, len(lanche)):#do 0 até acabar a tupla
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #fala a comida e a posição

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')# mesmo do d cima

print(len(lanche))#conta, ou seja, 5 lanches
print('Comi pra caramba!')
#index - procura numa tupla
