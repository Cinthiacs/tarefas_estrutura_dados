'''Em uma eleição para síndico de um prédio existem quatro candidatos. 
Os votos são informados por meio de código. Os códigos utilizados são: 1 , 2, 3, 4 
- Votos para os respectivos candidatos (você deve montar a listagem. Ex: 1 – Candidato A, 2-
Candidato B, 3-Candidato C, 4-Candidato D, 5 - Voto Nulo, 6 - Voto em Branco).
Faça um programa que calcule e mostre:
• O total de votos para cada candidato;
• O total de votos nulos;
• O total de votos em branco;
• A percentagem de votos nulos sobre o total de votos;
• A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.
'''

import random

lista_candidatos = ['Candidato 1','Candidato 2','Candidato 3','Candidato 4','Voto Nulo','Voto em Branco']

lista_votacao = [0,0,0,0,0,0]

resultado_votacao = {}

#Adiciono números aleatórios para cada candidato:

for i in range (len(lista_votacao)):
    lista_votacao[i] = random.randint(0,200)
    print(f'{lista_candidatos[i]} = {lista_votacao[i]}')

print(f'Total de votos: {(sum(lista_votacao))}')

print(f'Percentagem de votos nulos sobre o total de votos {round(lista_votacao[4]/sum(lista_votacao)*100)}%')

print(f'A percentagem de votos em branco sobre o total de votos {round(lista_votacao[5]/sum(lista_votacao)*100)}%')