"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:

a) - salário bruto.
b) - quanto pagou ao INSS.
c) - quanto pagou ao sindicato.
d) - o salário líquido.
e) - calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario = float(input('Digite o valor do seu salário por hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

bruto = salario * horas
IR = bruto * 0.11
INSS = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - IR - INSS - sindicato

print(f'\t+ Salário Bruto:   R$ {bruto:.2f}\n'
      f'\t- IR (11%):        R$ {IR:.2f}\n'
      f'\t- INSS (8%):       R$ {INSS:.2f}\n'
      f'\t- Sindicato (5%):  R$ {sindicato:.2f}\n'
      f'\t= Salário Líquido: R$ {liquido:.2f}')
