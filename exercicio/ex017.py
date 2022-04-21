import emoji
from math import hypot
print(emoji.emojize('CALCULAR HIPOTENUSA :triangular_ruler:', use_aliases=True))
co = float(input('Informe o Cateto Oposto do Triângulo Retângulo:'))
ca = float(input('Informe o Cateto Adjacente do Triângulo Retângulo:'))
hipo = hypot(co, ca)
print('A hipotenusa do Triângulo Retângulo é de {:.2f} '.format(hipo))
