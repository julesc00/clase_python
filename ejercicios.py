"""
Ejercicios
"""


"""
Ejercicio 001

Pedir nombre al usuario y mostrar e imprimir el siguiente mensaje: Hola [nombre]
"""


def obtener_nombre():
    nombre_usuario = input("Ingrese su nombre por favor: ")
    print("Hola ", nombre_usuario)


obtener_nombre()

"""
Ejercicio 002

Pedir al usuario su nombre, después pedirle su apellido y mostrar el 
siguiente mensaje: Hola [nombre] [apellido]
"""


def obtener_nombre_completo():
    pass


"""
Ejercicio 004 

Pedir al usuario que ingrese dos números. Sume los dos números y muestre 
el resultado como: El total es [resultado].
"""


def sumar():
    valor1 = int(input("Ingrese el primer número: "))
    valor2 = int(input("Ingrese el segundo número: "))
    total = valor1 + valor2
    print(f"El total es: {valor1 + valor2}")
    print("El total es: {}".format(valor1 + valor2))
    print("El total es: ", valor1 + valor2)
    print("El total es: ", total)


sumar()

"""
Ejercicio 005

Pedir al usuario que ingrese tres números. Sume todos los primeros dos 
números y luego multiplique el total por el último. Muestre el resultado 
como: La respuesta es [resultado]
"""


def sumar_y_multiplicar():
    pass
