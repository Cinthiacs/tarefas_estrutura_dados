'''2) Crie um método na classe já implementada que some todos os valores
ÍMPARES de uma lista encadeada e retorne o valor dessa soma.'''

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
soma_impares = 0 #Variável para armazenar o valor da soma dos ímpares

while True:

    escolha_usu = input('Olá Caro Usuário!\r\n'\
                        'Insira um número inteiro para inserir na lista, caso for número par, o programa aceitará: \r\n')
    
    try:
        escolha_usu = int(escolha_usu)
        if escolha_usu % 2 != 0:
            print(f'O número {escolha_usu} é impar, então será inserido na lista\r\n')
            lista.insert_before(escolha_usu)
           
            soma_impares += escolha_usu
            print(lista)
            print(f'Soma dos números ímpares inseridos: {soma_impares}')

        else:
            print(f'O número {escolha_usu}, é par, então será ignorado.')


    except ValueError:
        print('Entrada inválida. Por favor, insira uma escolha válida:')
