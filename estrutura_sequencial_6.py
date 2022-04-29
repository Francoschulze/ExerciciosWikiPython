"""
Faça um Programa que peça o raio de um círculo, calcule e mostre a sua área.
"""

# Fórmula para o cálculo da área
# area = π * r²

raio = float(input('Digite o raio da circunferência: '))

# Como o valor de pi é irracional, eu arredondei
# O valor: 3.1415926535897932384626433832795
area = 3.14 * raio ** 2

print(f'A área da circunferência é: {area} ')
