'''Lista duplamente encadeada é uma forma de estrutura de dados onde
cada elemento possui, o espaço de armazenamento da informação e um espaço
de armazenamento a referencia da localização de memoria onde se encontra o próximo
elemento da lista e outro espaçõ de referencia da localização de memoria onde se encontra
o elemento anterior.'''
#A principal diferença de uma lista simples:
#É a maior facilidade de navegação, que é feita por dois ponteiros
#O inicio/head e fim/end.


class DoubleNode:
    
    def __init__(self, data):
       self.data=data     
       self.next=None       #def __init__ sendo a função contrutor
       self.later=None

    def __str__(self):
        return str(self.data)   

class DoubleLinkedList:
    def __init__(self, max_length=None, force_type=None):
        self.head = None
        self.end = None
        self.__length = 0               #def __init__ sendo a função contrutor
        self.max_length = max_length
        self.force_type = force_type

    def is_empty(self):
        if self.head is None:
            print('A lista está vázia')
            print('-------------')
            return True                 #fuction is_empty para retornar se a lista esta vazia ou não
        print('A lista não está vázia')
        print('-------------')
        return False    

    def validate(self, data=None, index=None):
        if self.max_length and self.__length >= self.max_length:
            raise Exception('O número maximo de elementos já foi atribuido')
        if self.force_type and type(data) is not self.force_type:
            raise TypeError('O tipo não é válido')
        if index and index > self.__length - 1:
            raise IndexError('Index não existe na lista')

            #validate para avaliar se a lista está no tipo adequado

    def append(self, data):
        self.validate(data=data)
        new_node= DoubleNode(data)
        if self.__length == 0:
            self.head = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            new_node.later = self.end
            self.end = self.end.next
        self.__length += 1
        #fuction append para adicionar elementos no fim da lista

    def insert_for_index(self, index, data):
        if index < 0 or index > self.__length:
            raise IndexError("Index out of range")
        new_node = DoubleNode(data)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.end = new_node
            else:
                new_node.next = self.head
                self.head.later = new_node
                self.head = new_node
        elif index == self.length:
            self.end.next = new_node
            new_node.later = self.end
            self.end = new_node
        else:
            momentary_node = self.head
            for i in range(index-1):
                momentary_node = momentary_node.next
            new_node.next = momentary_node.next
            new_node.later = momentary_node
            momentary_node.next.later = new_node
            momentary_node.next = new_node
        self.__length += 1

        #fuction insert_for_index para adicionar elementos pelo index

    def length(self):
        if self.head == None:
            return 0
        momentary = self.head
        total = 0

        while momentary:
            total+=1
            momentary=momentary.next
        return total

        #fuction length para retornar o tamanho exato da lista

    def the_list(self):
         node_data = []
         momentary = self.head

         while momentary:
            node_data.append(momentary.data)
            momentary = momentary.next
         return node_data

        #fuction the_list para organizar a lista em uma unica linha no terminal

    def other_list(self):
        node_data_new = []
        momentary = self.head

        while momentary:
            node_data_new.append(momentary.data)
            momentary = momentary.next
        return node_data_new   

        #fuction other_list para organizar outra lista, que vai ser usada na  fuctino extender 

    def reverse(self):
        if self.head is None:
            print('A lista não possui elementos para inverter')
            return 0
        momentary = self.head
        new_node = momentary.next
        momentary.next = None
        momentary.later = new_node
        while new_node != None:
            new_node.later = new_node.next
            new_node.next = momentary
            momentary = new_node
            new_node = new_node.later
        self.head = momentary

        #fuction reverse para da output na lista original de forma inversa (de tras para frente)

    def display(self):
        object = self.head
        if object is None:
            print('Lista não possui elementos')
        while object:
            print(object.data)
            object=object.next
        print('\033[1;35;40m**************************\033[m')

        #fuction display para aparecer a lista no terminal

    def insert_at_start(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            print('Nó inserido')
            return
        new_node = DoubleNode(data)
        new_node.next = self.head
        self.head.later = new_node
        self.head = new_node 

        #fuction insert_at_start para adicionar elementos no inicio da lista

    def insert_at_end(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            return
        momentary = self.head
        while momentary.next != None:
            momentary = momentary.next
        new_node = DoubleNode(data)
        momentary.next = new_node
        new_node.later = momentary

        #Fuction insert_at_end para adicionar elemento no fim da lista

    def delete_element_by_start(self):
        if self.head == None:
            print('A lista não possui elementos para deletar')
            return
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None    

        #fuction delete_element_by_start para deletar/remover o primeiro elemento da lista    

    def delete_element_by_end(self):
        if self.head == None:
            print('A lista não possui elementos para deletar')        
            return
        if self.head.next == None:
            self.head = None
            return
        momentary = self.head
        while momentary.next != None:
            momentary = momentary.next
        momentary.later.next = None

        #fuction delete_element_by_end deletar/remover o último elemento da lista

    def delete_element_by_value(self, value):        
        if self.head == None:
            print('A lista não possui elementos para deletar')
            return
        if self.head.next == None:
            if self.head.item == value:
                self.head = None
            else:
                print('Item não existe')
            return            
        if self.head.data == value:
            self.head = self.head.next
            self.head.later = None
            return

        momentary = self.head
        while momentary.next != None:
            if momentary.data == value:
                break
            momentary = momentary.next
        if momentary.next != None:
            momentary.later.next = momentary.next
            momentary.next.later = momentary.later
        else:
            if momentary.data == value:
                momentary.later.next = None
            else:
                print('Elemento não existe na lista')
                print('***************') 

    #fuction delete_element_by_value deletar algum elemento pelo valor 
    #Ex.: lista=[1,2,3,4,5]; lista.delete_element_by_value(3)

    def append_for_extend(self, data):
        self.validate(data=data)
        new_node = DoubleNode(data)    
        new_node.next = None

        if self.head==None:
            new_node.later = None
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.later = last_node
        return 

    #fuction append_for_extend para a função extend usar para adicionar uma other_list na the_list

    def extend(self, other_list):
        if not other_list:
            return
        for data in other_list:
            self.append_for_extend(data)

    #fuction extend para extender a lista, adicionando o other_list no final da the_list

    def clear(self):
        momentary = self.head
        while momentary:
            empty_list = momentary.next
            momentary.later = momentary.next = None
            momentary.data = None
            momentary = empty_list
        self.head = self.end = None
        print('----------------------')
        print('\033[1;36;40mA lista foi totalmente limpa\033[m')
        input('\033[1;36;40mPressione ENTER para sair...\033[m')
        print('----------------------')


    #fuction clear limpar completamente a lista, deixando-a vazia

    def update(self, index, data):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of range")
        momentary_node = self.head
        for i in range(index):
            momentary_node = momentary_node.next
        momentary_node.data = data

    #fuction update atualizar um determinado elemento na lista, através do index    