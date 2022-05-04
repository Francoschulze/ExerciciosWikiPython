"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de "1 litro para cada 6 metros quadrados"
e que a tinta é vendida em "latas de 18 litros", que custam R$ 80,00 ou em "galões de 3,6 litros", que custam "R$ 25,00".
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    a) - comprar apenas latas de 18 litros;
    b) - comprar apenas galões de 3,6 litros;
    c) - misturar latas e galões, de forma que o desperdício de tinta seja menor.
    d) - Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

Obs: Exercício que requer muita lógica e paciência.
Dê uma fatiada nos problemas e faça com calma e vai conseguir realizar o exercício!
"""

# Importando o módulo math
# Módulo do próprio python
import math

area_a_pintar = int(100)
# Calculando os 10% de folga que deveremos utilizar como parâmetro

area_a_pintar_folga = area_a_pintar * 1.1

# Area dividido por 6 vai retornar a quantidade em litros
litros_tinta = area_a_pintar_folga / 6

# Utilizando math.ceil() a função do módulo math para arredondar valores para cima
# Latas de tinta
latas_tinta = math.ceil(litros_tinta / 18)

# Calculando o valor das latas de tinta
preco_latas = latas_tinta * 80

print(f'Você deverá usar {latas_tinta} latas de tinta e o preço será: R$ {preco_latas} ')

# Galões de tinta
# Aqui usaremos o mesmo raciocínio acima
galoes_tinta = math.ceil(litros_tinta / 3.6)
preco_galoes = galoes_tinta * 25
print(f'Você deverá usar {galoes_tinta} galões de tinta e o preço será: R$ {preco_galoes} ')

# Latas e galões otimizando a compra
# Agora vamos usar a função math.floor do módulo math
# Para arredondar para baixo e otimizar para a mistura com galões
numero_latas = math.floor(litros_tinta / 18)
valor_latas = numero_latas * 80
litros_restantes = litros_tinta % 18
numero_galoes = math.ceil(litros_restantes / 3.6)
valor_galoes = numero_galoes * 25

preco_latas_galoes = valor_latas + valor_galoes

print(f'Você deverá usar {latas_tinta} latas de 18 litros e'
      f'{numero_galoes} de 3,6 litros no valor de R$ {preco_latas_galoes}')
