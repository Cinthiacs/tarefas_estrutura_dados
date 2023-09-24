'''2) Escreva um programa em PYTHON que leia números inteiros e só armazene
aqueles que forem pares em uma LISTA ENCADEADA. A entrada de dados deve
ser interrompida quando o usuário informar o número zero ou esgotar a
quantidade definida de elementos a serem armazenados na estrutura. Por
último, imprima os elementos existentes na lista encadeada criada.
'''

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
lista = ListaEncadeada()

while True:

    escolha_usu = input('Olá Caro Usuário!\r\n'\
                        'Insira um número inteiro para inserir na lista, caso for número par, o programa aceitará: \r\n')
    
    try:
        escolha_usu = int(escolha_usu)
        if escolha_usu %2 == 0:
            print(f'O número {escolha_usu} é par, então será inserido na lista\r\n')
            lista.insert_before(escolha_usu) 
            print(lista)

        else:
            print(f'O número {escolha_usu} não é par, então será inserido na lista')


    except ValueError:
        print('Entrada inválida. Por favor, insira uma escolha válida (1, 2, 3 ou 4).')