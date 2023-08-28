'''Faça um programa com uma função que, dado um conjunto de N números
inseridos pelo usuário, determine o menor valor, o maior valor e a soma dos valores.
'''

def calcular_valores(lista):
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    return menor, maior, soma

num_usu = []

for n in range(3):
    while True:
        num_digt = input('Olá usuário(a), digite um número inteiro abaixo: \r\n')

        if num_digt.isdigit():
            num_usuario = int(num_digt)
            num_usu.append(num_usuario)
            break

        else:
            print('Voce digitou incorretamente')

menor_valor, maior_valor, soma_valores = calcular_valores(num_usu)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")