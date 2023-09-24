'''3) Escreva um programa em PYTHON que crie e preencha uma pilha e remova
os elementos da pilha e coloque na lista encadeada e na sequência imprima
os elementos existentes na lista.'''

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push (self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class NodeList:
   def __init__(self, data = 0, next = None):
       self.data = data
       self.next = next
       
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return '[' + ' | '.join(nodes) + ']'
    
    def insert_before(self,new_data):
        new_node = NodeList(new_data)
        new_node.next = self.head
        self.head = new_node
lista = ListaEncadeada()



pilha = Stack()

numeros_inseridos = [5,6,7,8]

for numero in numeros_inseridos:
    pilha.push(numero)

while not pilha.isEmpty():
    numero = pilha.pop()
    lista.insert_before(numero)
    
   
print(f'A sequencia da Lista Encadeada é: {lista}\r\n')


