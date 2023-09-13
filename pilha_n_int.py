''' Escreva um programa em PYTHON que leia números inteiros e
armazene em uma pilha. A entrada de dados deve ser interrompida
quando o usuário informar o número zero ou esgotar a quantidade
definida de elementos a serem armazenados na estrutura (caso quiser
definir uma quantidade). Por último, imprima os elementos na ordem
em que foram removidos da pilha.
'''

from inspect import stack

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push (self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def print_stack(self):
        while not self.isEmpty():
            print(self.pop(), end='\n')
        print()

    
numeros = Stack()

while numeros.size() < 5:           
    num_usu = input ('Olá Usuário, digite um numero inteiro: \r\n')

    if num_usu == '0':
        print('O programa foi encerrado')
        break

    try:
        numero_digitado = int(num_usu)
        numeros.push(numero_digitado)

    except Exception as e:
        print (f'Voce digitou um valor invalido {e}')
        continue

print('Elementos na ordem em que foram removidos da pilha: \r\n')
numeros.print_stack()