#dict que retorna o valor da nota do aluno
print('-' * 25)
print('{:^25}'.format('SITUAÇÃO DOS ALUNOS'))
print('-' * 25)
dados = {}
dados['nome']= str(input('Nome do aluno:'))
dados['media'] = float(input('Digite a media do aluno:'))
#lembrar que é float
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-=' * 25)
for k, v in dados.items():
    print(f'  - {k} é igual a {v}.')
#corrigido