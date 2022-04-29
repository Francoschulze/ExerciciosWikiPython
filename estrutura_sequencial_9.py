"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
Fórmula: C = 5 * ((F-32) / 9).
"""
# Solicitando a temperatura em graus Fahrenheit
fahre = int(input('Digite a temperatura em graus Fahrenheit: '))

# Realizando o cálculo e guardando na variável celsius
celsius = (fahre - 32) * 5 / 9

# Mostrando os dados na tela com a formatação sem casas decimais
print(f'A temperatura {fahre}°F em graus celsius é: {celsius:.0f}°C ')
