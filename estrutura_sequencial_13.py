"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

# Solicitando genero do usuário
genero = input('Digite [M] para homem ou [F] para mulher: ')

# Teste lógico para homem e mulher
if genero in 'Mm':
    altura_homem = float(input('Digite sua altura em metros: '))
    homem = 72.7 * altura_homem - 58
    print(f'O seu peso ideal é: {homem:.2f}')

elif genero in 'Ff':
    altura_mulher = float(input('Digite sua altura em metros: '))
    mulher = 62.1 * altura_mulher - 44.7
    print(f'O seu peso ideal é: {mulher:.2f}! ')

else:
    print('Opção inválida!')
