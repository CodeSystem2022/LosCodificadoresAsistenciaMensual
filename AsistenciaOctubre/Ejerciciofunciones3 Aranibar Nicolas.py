# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendete usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5 debe imprimir
# 5
# 4
# 3
# 2
# 1
# En caso de ser numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprimir nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1) #Caso Recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto..')
imprimir_numeros_recursivos(1)