from datetime import date
from time import sleep
atual = date.today().year
print('-=' * 20)
print('\033[35mCONTAGEM REGRESSIVA PARA O ANO NOVO !!!\033[m')
print('-=' * 20)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[33mFELIZ {}!!!\033[33m'.format(atual))
'''corrigido'''
