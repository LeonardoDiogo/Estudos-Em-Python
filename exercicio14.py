dados = float(input('qual a temperatura em ºC'))
F = (1.8 * dados) + 32
K =  dados + 273.15

print(f'a temperatura de {dados} corresponde a {F:.2f}')
print(f'e corresponde a {K:.2f} em Kelvin')
