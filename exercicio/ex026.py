frase = str(input('Digite uma frase:')).strip().upper()
print('Analisando frase...')
print('A sua frase contém {} letra(s) "a" '.format(frase.count('A', 0)))
print('Em sua frase, a primeira palavra com "a" é {}'.format(frase.find('A')+1))
print('Em sua frase, a última palavra com "a" é {}'.format(frase.rfind('A')+1))
'''corrigido'''

