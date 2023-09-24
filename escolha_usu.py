'''Implemente um programa em Python que utiliza a classe apresentada em
aula para implementar uma lista encadeada. O programa deve mostrar ao
usuário quatro opções. Se o usuário escolher 1, a lista deve ser impressa; se
escolher 2, ele deve entrar com o valor do conteúdo do novo elemento da
lista; se escolher 3, ele deve entrar com o valor do conteúdo a ser removido
da lista; se escolher 4, ele deve entrar com um valor a ser buscado na lista
e receber o retorno se o elemento foi ou não encontrado.'''

#Criando nó na lista
class NodeList:
   def __init__(self, data = 0, next = None):
       self.data = data
       self.next = next

    #def __repr__(self):
     #  return '%s - %s' % (self.data,self.next)
    
#Inserindo um elemento na nó da lista:

#node = NodeList (10)
#print(node)

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

    def insert_after (self,node_prev,new_data):
        new_node = NodeList(new_data)
        new_node.next = node_prev.next
        node_prev.next = new_node

    def search (self, data_search):
        current_node = self.head
        while current_node and current_node.data != data_search:
            current_node = current_node.next
            return current_node

    #node a ser removido  
    def remove(self,value):
        current_node = self.head
        prev_node = None
        while current_node:
            if prev_node:
                prev_node.next = current_node.next

            else:
                self.head = current_node.next   
                return #elemento vazio sai do loop
            
            prev_node = current_node
            current_node = current_node.next

        print(f'O elemento {value} não foi encontrado na lista.')


    def search (self, search_value):
        current_node = self.head
        while current_node:
            if current_node.data == search_value:
                return True #Caso encontre na lista
            current_node = current_node.next
        return False #Caso não encontre na lista


lista = ListaEncadeada()

while True:

    escolha_usu = input('Olá Caro Usuário!\r\n'\
                        'Insira 1 para imprimir a lista\r\n'\
                        'Insira 2 para inserir um novo conteúdo na lista\r\n'\
                        'Insira 3 para remover um ítem da lista\r\n'\
                        'Insira 4 para buscar um ítem na lista, e receba um retorno se ele existe\r\n')

    #Converte escolha do usuario para número inteiro
    try:
        escolha_usu = int(escolha_usu)

        if escolha_usu == 1:
            print(lista)
       
        elif escolha_usu == 2:
            item_usu = input('Digite um novo ítem a ser inserido abaixo: \r\n')   
            lista.insert_before(item_usu)     

        elif escolha_usu == 3:
            remove_usu = input(f'Escolha e digite um ítem abaixo para remover:\r\n{lista} \r\n')

            try:
                remove_usu = int(remove_usu)
                lista.remove(remove_usu)
                
            except ValueError:
                print('Entrada inválida. Por favor, insira um número válido para remover.')

        elif escolha_usu == 4:
            busca_usu = input(f'Digite um número abaixo para procurar se existe na lista:\r\n')
            if lista.search(busca_usu):
                print(f'O elemento: {busca_usu} foi encontrado na lista')
            else:
                print(f'O elemento {busca_usu} não foi encontrado na lista')

            
        if lista.head is None:
            novo_item_usu = input(f'A lista está vazia, insira um ítem abaixo: \r\n')
            novo_no = NodeList(novo_item_usu)
            lista.head = novo_no    

    except ValueError:
        print('Entrada inválida. Por favor, insira uma escolha válida (1, 2, 3 ou 4).')

    

   