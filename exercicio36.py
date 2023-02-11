casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa} em {anos} anos')
print(f'a prestação sera R${prestação}')
if prestação <= minimo:
    print('Emprestimos pode ser CONCEDIDO')
else:
    print('emprestimo NEGDO')
