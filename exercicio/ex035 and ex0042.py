print('Analisando o triângulo')
s1 = float(input('Informe o primeiro seguimento:'))
s2 = float(input('Informe o segundo seguimento:'))
s3 = float(input('Informe o terceiro seguimento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segementos acima podem formar triângulo', end=' ')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
