class Persona2:
    def __int__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        return self._edad


persona1 = Persona2('Ariel', 'Betancud', 41)
print(persona1.nombre)  # Llamamos al metodo getter
persona1.nombre = 'Juan Pedro'  # Llamamos al metodo setter
print(persona1.nombre)
print(persona1.mostrar_detalles())
# Atributo read-only (solo lectura) seria la edad proque no tiene el metodo set
print(persona1.edad)

# Tarea crear tres objetos mas, utilizando los metodos getter and setter
# para modificar, y mostrar los cambios con el metodo mostrar detalles

# Obejeto numero 1 de la tarea
persona2 = Persona2('Flor', 'Romero', 23)
persona2.nombre = 'Florencia'
persona2.apellido = 'Romery'
persona2.edad = 22
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona2.mostrar_detalles())

# Obejto numero 2 de la tarea
persona3 = Persona2('Caro', 'Felisa', 21)
persona3.nombre = 'Carolina'
persona3.apellido = 'Felix'
persona3.edad = 31
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
print(persona3.mostrar_detalles())

# Obejto numero 3 de la tarea
persona4 = Persona2('Naty', 'Lucero', 35)
persona4.nombre = 'Natalia'
persona4.apellido = 'Lucero'
persona4.edad = 33
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
print(persona4.mostrar_detalles())
