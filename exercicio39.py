from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento'))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
    print('Voce tem que se alistar imediatamente')

elif idade < 18:
    saldo = 18 - idade
    print(f'ainda faltam {saldo} anos para o alistamento')

elif idade > 18:
    saldo = idade - 18
    print(f'voce ja deveria ter se alistado a {saldo}')
