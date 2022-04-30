"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) - o produto do dobro do primeiro com metade do segundo.
b) - a soma do triplo do primeiro com o terceiro.
c) - o terceiro elevado ao cubo.
"""

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))
num_3 = float(input('Digite um número real: '))

# Cálculando e guardando os resultados nas variáveis
a = (num_1 * 2) * (num_2 / 2)
b = num_1 * 3 + num_3
c = num_3 ** 3

# Mostrando os dados na tela
print(f'Letra a: {a} ')
print(f'Letra b: {b} ')
print(f'Letra c: {c} ')
