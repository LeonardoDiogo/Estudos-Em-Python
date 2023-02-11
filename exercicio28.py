from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'* 20)
print('vou pensar em um numeo entre 0 e 5 tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('em que numero eu pensei?'))
sleep(3)

if jogador == computador:
    print('PARABENS voce acertou')
else:
    print(f'eu GANHEI eu pensei no numero {computador} e nao no {jogador}')

