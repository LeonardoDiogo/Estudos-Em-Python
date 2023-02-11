preço = float(input('preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3 x ou mais no cartao''')
opção = int(input('Qual é a oção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'sua compra sera parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas Parcelas? '))
    parcela = total / totalparc
    print(f'sua compra sera parcelada {totalparc}x de R${parcela:.2f}c/juros')
    print(f'Sua compra de R${preço:.2f} vai custar {total} no final')
