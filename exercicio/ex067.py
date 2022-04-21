#tabuada que ao adicionar números negativos é encerrada
print('=-=' * 10)
print('          TABUADA     ')
print('=-=' * 10)
t = numero = 0
while True: 
    numero = int(input('>>Digite o numero para ver a tabuada até o 10:'))
    if numero <= -1:
        break
    for t in range(1, 11):
        print(f' {numero} X {t} = {numero*t}')
    print('=' * 50)
print('babou!')