num = int(input('Digite um numero inteiro: '))
print('''escolha uma das bases para converção
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('sua opçao: '))
if opçao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertida para OCTAL é igual a {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECUMAL é igual a {hex(num)[2:]}')
else:
    print('opçao invalida. Tente novamente')
