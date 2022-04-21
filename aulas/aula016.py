#aula 16 | Tuplas
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
               0        1       2     3
c = 0
print(lanche[0]) #hamburguer #teoria
print(lanche[0:2]) #hmabuguer, suco #último elemento será ignorado
print(lanche[1:]) #suco, pizza, pudim #comece o que pede, e vá até o final
print(lanche[-1]) #pudim # -4 hamurguer. -3 = suco...
len(lanche) = 4 #cada coisa que tem dentro
for c in lanche:
    print(c) #hamburguer [0]
    #voltando e trocando o [0] para [1]
    print(c) #suco #loop infinito da lista até acabar saindo e seguindo o programa

# As tiplas são IMUTÁVEIS

() - tupla
[] - list
{} - dicionary
