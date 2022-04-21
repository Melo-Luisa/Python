import emoji
print(emoji.emojize(':city_sunrise: Sua Cidade possui "SANTO" :city_sunset:', use_aliases= True))
c = str(input('Informe o nome da sua cidade: ')).strip()
print(c[:5].upper() == 'SANTO')

