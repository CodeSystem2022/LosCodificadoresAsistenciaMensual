class Persona: # creamos una clase
   def __init__(self, nombre, apellido, edad):#se lo llama metodo init dunder
       self.nombre = nombre
       self.apellido = apellido
       self.edad = edad
Persona1 = Persona ("Daiana", "Raya", "33")
print(Persona1.nombre)
print(Persona1.apellido)
print(Persona1.edad)
print(f"El objeto1 de la clase Persona:{Persona1.nombre} {Persona1.apellido} Su edad es  {Persona1.edad}")
Persona2 = Persona("Pepe", "Gonzalez", 42)
print(f"El objeto2 de la clase Persona:{Persona2.nombre} {Persona2.apellido} Su edad es  {Persona2.edad}")

Persona1.nombre = "liliana"
Persona1.apellido = "Buccella"
Persona1.edad = 40
print(f"El objeto1 modificado de la clase Persona:{Persona1.nombre} {Persona1.apellido} Su edad es  {Persona1.edad}"

