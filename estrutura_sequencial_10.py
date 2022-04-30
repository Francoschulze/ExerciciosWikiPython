"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
Fórmula: F° = °C * 9 / 5 + 32
"""

celsius = int(input('Digite a temperatura em graus celsius: '))

# Realizando a conversão
fahrenheit = celsius * 9 / 5 + 32

print(f'A temperatura de {celsius}°C em graus Fahrenheit é: {fahrenheit:.0f}°F ')
