"""
Faça um programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

area = float(input('Digite a área em m²: '))

# 18L equivale a uma área de 54 m²
# Nesse caso se o resto da divisão for igual a 0
# Usaremos uma lata apenas, senão, acrescentaremos mais.
if area % 54 == 0:
    latas = area / 54
else:
    # Utilizei a função int para converter
    # O número para inteiro
    latas = int(area / 54) + 1

preco = latas * 80

print(f'Total de latas de tinta: {latas} latas de 18L\n'
      f'Total a pagar: R$ {preco:.2f} ')
