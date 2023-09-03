'''Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )'''

import random

temp_mes = [0,0,0,0,0,0,0,0,0,0,0,0]

mes = ['Janeiro','Fevereiro','Março','Abril','Maio', 'Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

min_temp_verao = 25
max_temp_verao = 40

min_temp_primavera = 20
max_temp_primavera = 30

min_temp_outono = 18
max_temp_outono = 27

min_temp_inverno = 10
max_temp_inverno = 22

temp_mes [mes.index('Dezembro')] = random.randint(min_temp_verao,max_temp_verao)
temp_mes [mes.index('Janeiro')] = random.randint(min_temp_verao,max_temp_verao)
temp_mes [mes.index('Fevereiro')] = random.randint(min_temp_verao,max_temp_verao)

temp_mes [mes.index('Março')] = random.randint(min_temp_outono,max_temp_outono)
temp_mes [mes.index('Abril')] = random.randint(min_temp_outono,max_temp_outono)
temp_mes [mes.index('Maio')] = random.randint(min_temp_outono,max_temp_outono)

temp_mes [mes.index('Junho')] = random.randint(min_temp_inverno,max_temp_inverno)
temp_mes [mes.index('Julho')] = random.randint(min_temp_inverno,max_temp_inverno)
temp_mes [mes.index('Agosto')] = random.randint(min_temp_inverno,max_temp_inverno)

temp_mes [mes.index('Setembro')] = random.randint(min_temp_primavera,max_temp_primavera)
temp_mes [mes.index('Outubro')] = random.randint(min_temp_primavera,max_temp_primavera)
temp_mes [mes.index('Novembro')] = random.randint(min_temp_primavera,max_temp_primavera)

media = sum(temp_mes)/12

print (f'A média da temperatura anual é: {media:.2f}')

print (f'Meses em que a temperatura foram acima da média: ')

for i in range(len(temp_mes)):
    if temp_mes[i] > media:
        print (f'{mes[i]}: {temp_mes[i]}°C')