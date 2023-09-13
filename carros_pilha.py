'''2) Construa um programa em PYTHON utilizando uma pilha que
resolva o seguinte problema:
Armazene as placas dos carros que estão estacionados numa rua sem
saída estreita. Dado uma placa verifique se o carro está estacionado na
rua. Caso esteja, informe a sequência de carros que deverá ser retirada
para que o carro em questão consiga sair.
'''

from inspect import stack

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push (self, item):
        self.items.append(item)

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
    
carros_pilha = Stack()

carros_pilha.push("ABD8484")
carros_pilha.push("SDE8481")
carros_pilha.push("EFE2324")
carros_pilha.push("WEW9549")
carros_pilha.push("AFE9111")

carro_usu = input('Insira uma placa para imprimir a sequência de saída: \r\n')
print(f"placa desejada {carro_usu}")

carro_usu = carro_usu.replace(' ', '').upper()


s = carros_pilha.search(carro_usu)
print (f'O carro está na posição {s}')

print(f'Carros que devem sair antes do seu')

while carros_pilha.isEmpty() is False:

    c = carros_pilha.pop()
    
    if c == carro_usu:
        break

    print(c)

