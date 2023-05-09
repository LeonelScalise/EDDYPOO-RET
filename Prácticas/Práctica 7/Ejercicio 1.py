#Implemente la clase Pila, como una secuencia de nodos anidados. En esta implementación el constructor de la clase Pila
#almacena la dirección al nodo cima. Los métodos de la clase Pila a realizar son: apilar, desapilar, esVacia, visualizar Pila.
#En esta Pila usted tiene almacenada la información de los libros de una biblioteca que están llegando para su organización y
#antes de ubicarlos en su librero se verifica que su estado e información este completa. De cada libro se debe tener: nombre/s
#autor, fecha de publicación, editorial y el número ISSN (código de 8 dígitos que sirven para identificar las publicaciones)


class Nodo():
    def __init__(self, dato = None, prox = None):
        self.dato = dato
        self.prox = prox
    
    def __str__(self):
        return str(self.dato)

class Pila():
    def __init__(self):
        nodo_inicio = Nodo("Este el primer objeto de la pila",[])
        self.headvalue = nodo_inicio

    def Apilar(self, libro):
        if libro in libro.listaCompletos and libro not in self.headvalue.prox:
            self.headvalue.prox.append(libro)
        else:
            print("El libro está incompleto, no fue verificado o ya se encuentra en la pila.")
            
    def desapilar(self, libro):
        if self.esVacia:
            print("La lista está vacía")
        else:
            self.headvalue.prox.pop(libro)

    def esVacia(self):
        return len(self.headvalue.prox) == 0

    def visualizarPila(self):
        print(self.headvalue.prox)
        
class libro():
    listaCompletos = []

    def __init__(self, nombre = "", autor = "", fecha_publi = "", editorial = "", ISSN = ""):
        self.nombre = nombre
        self.autor = autor
        self.fecha_publi = fecha_publi #faltaría validar que el dato ingresado sea una fecha
        self.editorial = editorial
        self.ISSN = ISSN #faltaría validar que sea de 8 digitos
    
    def verificacionCompletos(self):
        if self not in self.listaCompletos:
            if self.nombre != "" and self.autor != "" and self.fecha_publi != "" and self.editorial != "" and self.ISSN != "":
                self.listaCompletos.append(self)
            else:
                print("El libro está incompleto")
        else:
            print("El libro ya fue verificado")
