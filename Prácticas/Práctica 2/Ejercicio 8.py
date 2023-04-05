# Realizar una función que reciba como parámetros una lista de elementos y un elemento que se desea eliminar de la lista y retorne la lista con los elementos eliminados si coinciden con el parámetro que paso el usuario. El id de la lista antes de eliminar elementos ¿Debería ser el mismo id luego de que se eliminen elementos? ¿Por qué sí o por qué no?

def eliminar_elementos(lista, elemento):
    eliminados = []
    nueva_lista = []
    e = 0

    for i in range(0,len(lista)):
        if elemento == lista[i]:
            eliminados.append(elemento)
        else:
            nueva_lista.append(lista[i])
    
    for j in range(0, len(lista)):
        if elemento in lista:
            lista.remove(elemento)


    return print(eliminados,"\n",nueva_lista, lista)


eliminar_elementos([1,2,3,4,12,4,7,8,3,2,2], 2)

# No deberian tenes el mismo id porque cree un nuevo objeto para mostrar tanto los elementos eliminados como la lista con los que quedaron