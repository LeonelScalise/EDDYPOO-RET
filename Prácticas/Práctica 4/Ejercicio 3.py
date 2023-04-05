from datetime import datetime
import random

class Persona:

    dni_existentes = []

    def __init__(self, nacimiento, nombre = '', sexo = 'H'):

        self.nombre = nombre
        self.sexo = sexo
        self.dni = random.randint(10000000,99999999)
        self.nacimiento = datetime.strptime(nacimiento, '%d/%m/%y')

        if self.dni in self.dni_existentes:
            raise ValueError(f'El DNI {self.dni} ya se encuentra registrado')


    def mayor_edad(self):
        return self.edad >= 18
    
    def info_persona(self):
        return print('Nombre: {} \n DNI: {} \n Edad: {} \n Sexo: {}'.format(self.nombre, self.edad, self.dni, self.sexo))

Pepe = Persona("21/3/2011", "Jose")