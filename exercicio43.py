nome = input('Qual é seu nome?: ')
peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O seu imc {nome} é de {imc:.2f}')

if imc <= 18.5:
    print('voce esta com magreza')

elif 18.5 <= imc < 25:
    print('seu peso esta normal')

elif 25.0 <= imc < 30:
    print('voce esta em SOBREPESO')

elif 30.0 <= imc < 40:
    print('Voces esta com obesidade tipo 2')

else:
    print('Voces esta com obesidade tipo 3')
