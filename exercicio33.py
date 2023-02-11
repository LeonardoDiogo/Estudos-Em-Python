a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# maior que
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'o menor valor digitalizado foi {menor}')
print(f'o maior valor foi {maior}')
