from datetime import date
atleta = int(input('Informe o ano de nascimento do(a) atleta: '))
idade = date.today().year - atleta
if idade <= 9:
    print('O(a) atleta possui {} anos de idade e está na categoria \033[31mMIRIM\033[m!'.format(idade))
elif idade <= 14:
    print('O(a) atleta possui {} anos de idade e está na categoria \033[32mINFANTIL\033[m!'.format(idade))
elif idade <= 19:
    print('O(a) atleta possui {} anos de idade e está na categoria \033[32mJÚNIOR\033[m!'.format(idade))
elif idade <= 25:
    print('O(a) atleta possui {} anos de idade e está na categoria \033[33mSÊNIOR\033[m!'.format(idade))
else:
    print('O(a) atleta possui {} anos de idade e está na categoria \033[34mMASTER\033[m!'.format(idade))
