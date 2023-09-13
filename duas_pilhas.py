'''3) Escreva uma função que receba como parâmetro duas pilhas e
verifique se elas são iguais.
Duas pilhas são iguais se possuem os mesmos elementos, na mesma
ordem.
'''
from inspect import stack
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push (self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
        
    def search(self,content):

        if content not in self.items:
            return -1

        for i in range(len(self.items)):
            if self.items[i] == content:
                return i
            
    def print_stack(self):
        for i in range(len(self.items)-1,-1,-1):
            print(str(self.items[i]))

pilha1 = Stack()
pilha2 = Stack()

pilha1.push ('5')
pilha1.push ('6')
pilha1.push ('7')
pilha1.push ('8')

pilha2.push ('5')
pilha2.push ('6')
pilha2.push ('7')
pilha2.push ('8')


pilha1.print_stack()

while pilha1 and pilha2.isEmpty() is False:
    p1 = pilha1.pop()
    p2 = pilha2.pop()

    if p1 == p2:

        print(f'As pilhas são iguais {p1} {p2}')

    else:
        print('As pilhas são diferentes')
        break