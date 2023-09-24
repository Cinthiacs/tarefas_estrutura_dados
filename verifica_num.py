'''4) Crie um programa usando a linguagem PYTHON que peça ao usuário que informe um valor
inteiro e receba todos os valores digitados até que o usuário digite 0 (que representa que a
entrada de dados será interrompida). A cada valor digitado pelo usuário, faça a seguinte
manipulação:
- Se o valor for positivo e par, insira na pilha.
-Se o valor for positivo e impar, insira na fila.
-Se o valor for negativo, insira na lista encadeada.
- Se o valor for 0, não insira em nenhuma estrutura e encerre a entrada de dados.
Após a inserção dos dados em cada uma das estruturas de dados utilizadas, imprima a
quantidade de valores (itens) e os itens existentes em cada estrutura.
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
        if not self.isEm0pty():
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

#Criando nó na lista
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

pilha = Stack()
lista = ListaEncadeada()
num_impares = []

while True:

    escolha_usu = input('Olá Caro Usuário!\r\n'\
                        'Insira um número inteiro para inserir na lista, fila ou pilha: \r\n'\
                            'Ou digite 0 para encerrar e imprimir os dados: \r\n')
    
    try:
        escolha_usu = int(escolha_usu)
        if escolha_usu %2 == 0 and escolha_usu > 0:
            print(f'O número {escolha_usu} é par, e positivo então será inserido na pilha:')
            pilha.push(escolha_usu) 
            pilha.print_stack()

        elif escolha_usu %2 != 0 and escolha_usu > 0:
            print(f'O número {escolha_usu} é impar, e positivo então será inserido na fila:')
            num_impares.append(escolha_usu) 
            print(num_impares)

        elif escolha_usu < 0:
            print(f'O número {escolha_usu} é negativo, então será inserido na lista encadeada:')
            lista.insert_before(escolha_usu)
            print (lista)
        
        elif escolha_usu == 0:
            print('Programa encerrado\r\n')
            input('Digite qualquer tecla para encerrar...')
            break
                
        else:
            pass


    except ValueError:
        print('Entrada inválida. Por favor, insira uma escolha válida.')

print('Pilha:')
pilha.print_stack()

print('Lista:')
print(num_impares)

print('Lista Encadeada:')
print(lista)

