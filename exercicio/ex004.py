# dissecando uma variavel
a = input ('Digite algo:')
print('\033[31mO tipo primitivo desse valor é {}', type(a))
print('\033[32mSó tem espaços?', a.isspace())
print('\033[33mÉ um número?', a.isnumeric())
print('\033[34mÉ alfabetico?', a.isalpha())
print('\033[35mÉ alfanuméricos?', a.isalnum())
print('\033[36mÉ maiúscula?', a.isupper())
print('\033[30mÉ minúscula?', a.islower())
print('\033[7;30mEstá capitalizada?\033[m', a.istitle())

