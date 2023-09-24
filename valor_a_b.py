'''3) Crie um método na classe já implementada que receba por parâmetro dois
valores int (a e b) e remova de uma lista já preenchida todos os elementos cujo
valor esteja entre a e b'''

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

    #node a ser removido  
    def remove_elementos_entre(self,a,b):
        current_node = self.head
        prev_node = None

        while current_node:
            if a <= current_node.data <= b:
                #verifica se o valor está entre a e b para remover o nó
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                current_node = current_node.next

            else:
                prev_node = current_node
            current_node = current_node.next


lista = ListaEncadeada()

a = 10
b = 20 

lista.insert_before(5)
lista.insert_before(15)
lista.insert_before(25)
lista.insert_before(35)
lista.insert_before(45)

print(f'Lista original: {lista}')

lista.remove_elementos_entre(a,b)

print(f'Lista após a remoção: {lista} Retirando o número 15, pois se encontra entre 10 e 20 (a e b)')



