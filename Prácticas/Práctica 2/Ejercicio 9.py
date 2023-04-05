#Utilice la misma función del ejercicio anterior pero en vez de pasar como parámetro una lista, pase unacadena. ¿Obtiene el mismo resultado?¿Por qué? ¿Cuál es la diferencia entre la lista y la cadena?



def eliminar_elementos(string, elemento):
    
    if elemento in string:
        new_string = string.replace(elemento, '')

    return print(new_string,id(string), id(new_string))

eliminar_elementos("carrusel", "r")


#El id cambia porque estoy haciendo un objeto nuevo, pues los string son inmutables