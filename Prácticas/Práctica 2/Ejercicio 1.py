# Métodos que modifican una lista dada
# append() - remove() - clear() - sort() - insert()

# Ejercicio con .append()

lista_1 = ["AGREGAR", "ELEMENTO"]
lista_1.append("X")
print(lista_1)

lista_2 = ["REMOVER", "ELEMENTO", "X"]
lista_2.remove("X")
print(lista_2)

lista_3 = ["LIMPIAR", "LISTA", "X"]
lista_3.clear()
print(lista_3)

lista_4 = ["ORDENAR", "LISTA", "X"]
lista_4.sort()
print(lista_4)

lista_5 = ["INSERTAR", "ELEMENTO", "X"]
lista_5.insert(2, "A")
print(lista_5)
