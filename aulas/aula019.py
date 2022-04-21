#DICIONÁRIOS | TEORIA
#variaveis compostas
#estrutura de dados semelhantes a listas e tuplas, porém pode ser nomeados
#tuplas ()
#listas []
#dicionarios {}
dados = dict()
dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome']) #pedro
print(dados['idade']) #25
#append não funcionada
dados['sexo'] = 'M'
#remover
del dados['idade']
filme = {'titulo': 'Star Wars',
'ano':1977,
'diretor': 'George Lucas'
}
print(filme.values()) #retorna todos os VALORES
print(filme.keys())#nome do dicionário
print(filme.items())#itens(tudo: keys e valores)
for k, v in filme.items():
    print(f'O {k} é {v}')
    #o titulo é Star wars...
#         k         v
locadora = [{filme}]
#lista em dict
print(locadora[0]['ano'])#1977

#PRÁTICA
pessoas = {'nome': 'Luisa', 'sexo': 'F', 'idade': 18}
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')
#        A Luisa tem 18 anos.
print(pessoas.keys())
#      'nome', 'sexo', 'idade'
for k, v in pessoas.itens:
    #enumerate não existe
    print(f'{k} = {v}')

#copia
estado = {}
br = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla:'))
    br.append(estado.copy())
print(br)
#todos os dados add no dict
