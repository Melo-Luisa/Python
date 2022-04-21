#Teoria | LISTAS
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
lanche.append('cookie')#adicionar ao final
lanche.insert(0,'hot dog')#adicionar em qualquer posição desejada
del lanche[3] #deletar o 3º lanche
lanche.pop(3)#deletar o último (sem o valor), com o valor remove o valor apenas
lanche.remove('suco')#remover o valor
print(lanche)

valores = list(range(4, 11))#[4 - 5 - 6 - 7 - 8 - 9 - 10]
valores.sort() #organizado em ordem
valores.sort(reverse=True)#reverter o valor
len(valores)#contando os valores
