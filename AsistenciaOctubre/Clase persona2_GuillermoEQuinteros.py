# Clase n°10
# Lección 6: Persona 2
# Encapsulamiento y métodos Getter and Setter

""" Tarea 1: A lo dado en clase, hacer los métodos Get y Set para los 
atributos apellido y edad. """

class Persona2:
    def __init__(self, nombre, apellido, edad): # Método inicializador init para los atributos.
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalles(self):                 # Método mostrar detalles.
        print('Los datos a mostrar son los siguientes:')
        print(f'{self._nombre} {self._apellido}: {self._edad}')
    @property                                   # Decorador
    def nombre(self):                           # Método getter
        print('Estamos utilizando el método Get')
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):                   # Método setter
        print('Estamos utilizando el método Set')
        self._nombre = nombre
    @property                                   # Inicio tarea 1
    def apellido(self):
        print('Se utiliza el método Get')
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        print('Se utiliza el método Set')
        self._apellido = apellido
    @property                                   
    def edad(self):
        print('Se utiliza el método Get')
        return self._edad
    @edad.setter
    def edad(self, edad):
        print('Se utiliza el método Set')
        self._edad = edad
        
persona1 = Persona2('Ariel', 'Betancud', '41')
print(persona1.nombre)                        # Se obvían los (), por el property.
print(persona1.apellido)
print(persona1.edad)
persona1.nombre = 'Juan Pedro'
persona1.apellido = 'Gomez'
persona1.edad = '40'
print(persona1.mostrar_detalles())

''' Tarea 2: Crear 3 objetos más (personas 2, 3 y 4) utilizando los métodos
Getter and Setter para mostrar y modificar respectivamente y luego mostrar  
los cambios con el método mostrar_detalles. '''
    
persona2 = Persona2('Juan', 'De Silva', '41')
print(persona2.nombre)                        
print(persona2.apellido)
print(persona2.edad)
persona2.nombre = 'Joan'
persona2.apellido = 'Da Silva'
persona2.edad = '42'
print(persona2.mostrar_detalles())

persona3 = Persona2('Dana', 'Montaña', '21')
print(persona3.nombre)                        
print(persona3.apellido)
print(persona3.edad)
persona3.nombre = 'Dania'
persona3.apellido = 'Montañas'
persona3.edad = '23'
print(persona3.mostrar_detalles())

persona4 = Persona2('Ramiiro', 'Brabo', '36')
print(persona4.nombre)                        
print(persona4.apellido)
print(persona4.edad)
persona4.nombre = 'Ramiro'
persona4.apellido = 'Bravo'
persona4.edad = '35'
print(persona4.mostrar_detalles())
    