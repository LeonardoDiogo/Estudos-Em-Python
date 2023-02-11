distancia = float(input('qual é a ditancia da sua viagem? '))
print(f'voce esta prestes a comecar uma viagem {distancia}Km')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preco da sua passagem sera R${preço:.2f}')