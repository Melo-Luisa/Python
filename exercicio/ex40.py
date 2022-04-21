nome = str(input('Informe o nome do aluno(a):'))
nota1 = float(input('Informe a primeira nota do(a) {}:'.format(nome)))
nota2 = float(input('Informe a segunda nota do(a) {}:'.format(nome)))
m = (nota1 + nota2) / 2
if m < 5.0:
    print('O(A) aluno(a) {} está REPROVADO(A)! Sua nota média foi {:.1f}!'.format(nome, m))
elif m >= 7.0:
    print('O(A) aluno(a) {} está APROVADO(A)! Sua nota média foi {:.1f}!'.format(nome, m))
else:
    print('O(A) aluno(a) {} está de RECUPERAÇÃO! Sua nota média foi {:.1f}!'.format(nome, m))
