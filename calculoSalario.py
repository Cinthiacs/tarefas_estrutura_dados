'''Exercício 1
Obs.: Salário Bruto - Descontos = Salário Líquido.
Faça um Programa em Python que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$
IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$'''

nome = ''
sal_hora  = 0.0
hora_mes = 0

nome = input('Olá, seja bem vindo(a) Digite seu nome: \r\n')

sal_hora = float(input('Olá! '+ nome +' Digite o valor do quanto voce ganha por hora (utilize somente ponto): \r\n'))

hora_mes = int(input('Digite quantas horas voce trabalha por mês: \r\n'))

sal_bruto = (sal_hora * hora_mes)
imp_renda = (sal_bruto * 0.11)
inss = (sal_bruto * 0.08)
sindicato = (sal_bruto * 0.05)
sal_liq = (sal_bruto - imp_renda - inss - sindicato)

print('Salário Bruto: R$ {:.2f}'.format(sal_bruto)) 
print('IR (11%): R$ {:.2f}'.format(imp_renda))
print('INSS (8%): R$ {:.2f}'.format(inss)) 
print('Sindicato ( 5%): R$ {:.2f}'.format(sindicato)) 
print('Salário Liquido: R$ {:.2f}'.format(sal_liq))