from operator import imod


import math
angulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radian(angulo))
print(f'o angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'o angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'o angulo de {angulo} tem a tangente de {tangente:.2f}')

#pode tirar o math se voce importar apenas o sin cos tan
