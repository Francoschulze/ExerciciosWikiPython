"""
Tendo como dados de entrada a altura de uma pessoa em metros,
construa um algoritmo que calcule o peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = float(input('Digite sua altura: '))

# Calculando e guardando na variável
peso_ideal = 72.7 * altura - 58

# Mostrando os dados na tela com duas casas decimais
print(f'O seu peso ideal é: {peso_ideal:.2f} ')
