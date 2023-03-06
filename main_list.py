from lista_duplamente_encadeada_1VA import*
from time import sleep

myList=DoubleLinkedList()
myList.display()
print('ADICIONANDO ELEMENTOS NA LISTA')
print('***************')

sleep(2)

myList.append(30)
myList.append(40)
myList.append(50)
myList.append(60)
myList.append(70)
myList.append(80)
myList.display()

sleep(1)

myList.is_empty()
myList.display()
sleep(2)

print('Número de total de elementos na lista: ' + str(myList.length()))
print(myList.the_list())
print('***************')

sleep(1)

print('DELETAR O PRIMEIRO ELEMENTO')
print('***************')

sleep(1)

myList.delete_element_by_start()
myList.display()

sleep(1)

print('DELETAR O ÚLTIMO ELEMENTO')
print('***************')

sleep(1)

myList.delete_element_by_end()
myList.display()

sleep(1)

print('ADICIONAR ELEMENTO NO COMEÇO DA LISTA')
print('***************')

sleep(1)

myList.insert_at_start(20)
myList.display()

sleep(1)

print('ADICINOAR ELEMENTO NO FIM DA LISTA')
print('***************')

sleep(1)

myList.insert_at_end(90)
myList.display()

sleep(1)

print('DELETAR ELEMENTO POR VALOR')
print('***************')

sleep(1)

myList.delete_element_by_value(70)
myList.display()

sleep(1)


print('Número de total de elementos na lista: ' + str(myList.length()))
print(myList.the_list())
print('*****************')

sleep(1)

print('LISTA DE FORMA INVERSA')

sleep(1)

myList.reverse()
myList.display()

sleep(1)

print('EXTENDER A LISTA')

sleep(1)

myList.extend([10,20,30])
myList.display()

sleep(1)


print('Número de total de elementos na lista: ' + str(myList.length()))
print(myList.the_list())
print('*****************')

sleep(1)

print('ATUALIZAR VALOR NA LISTA')

sleep(1)

myList.update(2,100)
myList.display()

sleep(1)

print('INSERIR ELEMENTO PELO INDEX')

sleep(1)

myList.insert_for_index(3,450)
myList.display()

sleep(1)

print('LIMPAR A LISTA COMPLETA')

sleep(1)

myList.clear()
myList.display()