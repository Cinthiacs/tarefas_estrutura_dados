'''Em uma competição de salto a distância cada atleta tem direito a cinco saltos. O
resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. Informe qual foi o melhor e o pior salto. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
conforme o exemplo abaixo:
Exercícios
'''
import sys

saltos = [0,0,0,0,0]
saltos_usu = []


atleta =  (input('Olá Caro Usuário(a), Digite o Nome do atleta abaixo: \r\n'))

#funcao .strip verifica se a entrada esta vazia, após remover espaços em branco

while not atleta.strip(): 
    print('Você não digitou um nome válido. Programa encerrado.')
    sys.exit()


for s in range(len(saltos)):
    while True:
        saltos_digitados = input('Digite o numero em metros da distancia alcançada pelo atleta abaixo: \r\n')

        #Transformando o numero digitado pelo usu em um float
        try:
            #inserindo o numero na lista saltos_usu
            saltos_usu.append(float(saltos_digitados))
         
            break

        except ValueError:
            print('Voce digitou um valor inválido, digite novamente:\n')

media_saltos = sum(saltos_usu)/5

print(f'\r\nNome do Atleta: {atleta}\r\n')

print(f'Primeiro Salto: {saltos_usu[0]} m')
print(f'Segundo Salto: {saltos_usu[1]} m')
print(f'Terceiro Salto: {saltos_usu[2]} m')
print(f'Quarto Salto: {saltos_usu[3]} m')
print(f'Quinto Salto: {saltos_usu[4]} m\r\n')

print('Resultado Final:')
print(f'Atleta: {atleta}')
print(f'Saltos: {saltos_usu[0]} - {saltos_usu[1]} - {saltos_usu[2]} - {saltos_usu[3]} - {saltos_usu[4]}')
print(f'A média dos saltos: {media_saltos:.2f} m\r\n')

saltos_usu.sort

print(f'O pior salto foi de: {saltos_usu[0]:.2f} m\r\n')
print(f'O melhor salto foi de: {saltos_usu[4]:.2f} m\r\n')


 