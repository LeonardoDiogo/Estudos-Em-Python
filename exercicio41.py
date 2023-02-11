from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento'))
idade = atual - nascimento
print(f'O Atleta te {idade} anos ')

if idade <= 9:
    print('Classifiação MIRIN')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classifiação: MASTER')
