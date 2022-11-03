class Persona2:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Los datos son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):
       #print('Usamos get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
       #print('Usamos set')
        self._nombre = nombre

    @property
    def apellido(self):
       #print('Usamos get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
       #print('Usamos set')
        self._apellido = apellido

    @property
    def edad(self):
       #print('Usamos get')
        return self._edad

    @edad.setter
    def edad(self, edad):
       #print('Usamos set')
        self._edad = edad
    
'''
persona1 = Persona2('Lili', 'Buccella',45)
print(persona1.nombre)
persona1.nombre = 'Liliana'
print(persona1.nombre)
print(persona1.mostrar_detalles())
print(persona1.edad)
'''

#CREAR 3 OBJETOS MAS, UTILIZANDO LOS METODOS GETTER AND SETTER
#PARA MODIFICAR Y MOSTRAR LOS CAMBIOS EN EL MÉTODO  MOSTRAR DETALLES.

#OBJETO 1
persona2 = Persona2('Rodri','Torta',36)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona2.nombre = 'Rodrigo'
persona2.apellido = 'Tortosa'
persona2.edad = 38

print(persona2.mostrar_detalles())

#OBJETO 2
persona3 = Persona2('Lauty','Torta',12)
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
persona3.nombre = 'Lautaro'
persona3.apellido = 'Tortosa'
persona3.edad = 10

print(persona3.mostrar_detalles())

#OBJETO 3
persona4 = Persona2('Bauty','Torta Irib',15)
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
persona4.nombre = 'Bautista'
persona4.apellido = 'Tortosa Iribarren'
persona4.edad = 10

print(persona4.mostrar_detalles())




