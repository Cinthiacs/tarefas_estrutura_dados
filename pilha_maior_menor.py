'''Escrever uma função que receba como parâmetro uma pilha.
A função deve retornar o maior e menor elemento da pilha.
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

pilha = Stack

while pilha.size < 3:
    pilha_usu = input ('Olá Usuário, digite um numero inteiro: \r\n')

    try:
            pilha_digitada = int(pilha_usu)
            pilha.push(pilha_digitada)

    except Exception as e:
        print (f'Voce digitou um valor invalido {e}')
        continue

    p = pilha_digitada.pop()
