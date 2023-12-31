'''Faça um programa que carregue uma lista com os modelos de cinco carros
(exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o
consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com
um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para
percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando
um que a gasolina custe R$ 6,25 o litro. Abaixo segue uma tela de exemplo. O
disposição das informações deve ser o mais próxima possível ao exemplo. Os dados
são fictícios e podem mudar a cada execução do programa.
Exercícios
'''

carros = ['Corsa', 'Onix', 'Versa', 'Celta', 'Cobalt']
km_lt = ['10.3', '12.5', '12', '12.2', '8.5']

carros_km = []
km_total = 1000
km_p_lt = 6.25 

for c in range(len(carros)):
    carros_km.append([carros[c], float(km_lt[c])])

for i, carro_km in enumerate(carros_km, start=1):
    print(f'Veículo {i}\n{carro_km[0]}\nKm por Litro: {carro_km[1]} \n')

print('Relatório Final:\r\n')



for i, carro_km in enumerate(carros_km,start=1):
    consumo_carro = km_total / carro_km[1]
    custo = consumo_carro * km_p_lt
    print(f'{i} - {carro_km[0]} - {carro_km[1]} - {consumo_carro:.2f} - R$ {custo:.2f}\r\n')

