#cadastro de CTPS em PYTHON
#35 anos de contribuição
from datetime import date 
from time import sleep
today = date.today().year
lista = {}
lista['nome'] = str(input('Digite o seu nome:'))
Nascimento = int(input('Informe a seu anos de nascimento:'))
lista['ctps'] = int(input('Informe a sua CTPS (0 se não tiver):'))
lista['idade'] = today - Nascimento
if lista['ctps'] != 0:
    lista['contratação'] = int(input('Qual foi o ano de contrato:'))
    lista['salario'] = float(input('Qual o último salário: R$'))
    lista['Aposentar'] =  lista['idade'] + ((lista['contratação'] + 35) - today)
print('-=' * 25)
print('{:^25}'.format('INFORMAÇÕES'))
for i, v in lista.items():
    print(f'  -  {i} = {v}')
print('-=' * 25)
print('>>FINALIZANDO...')
sleep(0.5)
print('Babou')