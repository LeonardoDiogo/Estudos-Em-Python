nota1 = float(input('Primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno é {media:.1f}')
if 7 > media >= 5:
    print('O aluno esta em RECUPERAÇÃO')
elif media < 5:
    print('o aluno esta REPROVADO')
else:
    print('O alunoe esta APROVADO')
