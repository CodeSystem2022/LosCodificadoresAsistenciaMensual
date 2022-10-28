class Cubo:
    """
    Debe tener 3 atributos ancho, alto y profundo y un metodo que calcule el volumen
    La base y altura debe ser ingresada por el usuario y los objetos deben ser 3
    """
    def __init__(self, ancho, alto, prof):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = prof
    
    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad


ancho = int(input('Ingrese el ancho del cubo: '))
alto = int(input('Ingrese el alto del cubo: '))
profundidad = int(input('Ingrese la profundidad del cubo: '))
cubo1 = Cubo(ancho, alto, profundidad)
print(f'El volumen de cubo es: {cubo1.calcularVolumen()}')