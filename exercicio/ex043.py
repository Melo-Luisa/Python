from time import sleep
print('=-=' * 16)
print('CALCULANDO O SEU INDICE DE MASSA CORPORAL - \033[34mIMC\033[m')
print('=-=' * 16)
kg = float(input('Informe o seu peso atual: '))
h = float(input('Informe a sua altura atual:'))
print('ANALISANDO...')
sleep(2)
imc = kg / (h ** 2)
if imc <= 18.5:
    print('Você está \033[31mABAIXO DO PESO\033[m, seu IMC é de {:.1f}!'.format(imc))
elif imc <= 25:
    print('Você está no \033[32mNO PESO IDEAL\033[m, seu IMC é de {:.1f}!'.format(imc))
elif imc <= 30:
    print('Você está no \033[33mSOBREPESO\033[m, seu IMC é de {:.1f}!'.format(imc))
elif imc <= 40:
    print('Você está na \033[35mOBESIDADE\033[m, seu IMC é de {:.1f}!'.format(imc))
else:
    print('Você está em \033[1;4;31mOBESIDADE MÓRBIDA\033[m, seu IMC é de {:.1f}!'.format(imc))
#corrigido
