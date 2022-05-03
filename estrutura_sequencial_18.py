"""
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

arquivo = float(input('Digite o tamanho do arquivo em MB: '))
vel = int(input('Digite a velocidade em MB de sua internet: '))

# Fórmula:
# Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.
tempo = arquivo / (vel / 8)
# Convertendo de segundos para minutos
minutos = tempo / 60

print(f'O tempo aproximado de download será de {minutos:.2f} minutos.')
