"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
nota_3 = float(input('Digite sua terceira nota: '))
nota_4 = float(input('Digite sua quarta nota: '))
# Adicionando o cálculo para a variável média
# Não esquecer a ordem de precedência
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'Sua média foi: {media:.2f}')
