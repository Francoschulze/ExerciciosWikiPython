"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador
para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""

# Usaremos como entrada o peso de 68 kg
# Como o enunciado pediu apenas para ler as variáveis
# Não necessitamos fazer um teste de condição

peso = float(input('Digite o valor em kg: '))

excesso = float(peso - 50.00)
multa = float((peso - 50.00) * 4.00)

print(f'Você excedeu em {excesso:.2f} kg além do permitido que são 50.00 kg.\n'
      f'A multa para pagamento será de: R$ {multa:.2f}! ')

