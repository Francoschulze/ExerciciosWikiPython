"""
Faça um Programa que pergunte quanto a pessoa ganha por hora
e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês.
"""

valor_hora = float(input('Qual valor remunerado por hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

# Mostrando os dados na tela com f-strings
# Aqui fiz o cálculo direto na formatação com duas casas decimais
print(f'Teu salário mensal será de: R$ {valor_hora * horas:.2f} ')
