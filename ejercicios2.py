
def imprimir_pedazos_de_pizza_que_quedan():
    """
    Ejercicio 006
    Preguntar al usuario cuántos pedazos de pizza son con los que inició y
    cuántos pedazos se ha comido.
    Encuentra cuántos pedazos de pizza le quedan y muestra la respuesta
    en un formato amigable-al-usuario.
    """
    pass


def pedir_la_cuenta():
    """
    Ejercicio 007
    Pide al usuario su nombre y edad. Súmale 1 a su edad y que la salida muestre:
    [nombre] será [nueva edad] en su próximo cumpleaños.
    """
    pass


def pedir_edad():
    """
    Ejercicio 008
    Pedir la edad al usuario, y si esta es menor a 18 años,
    mostrarle un mensaje que es menor de edad y no puede acceder
    al antro, pero si tiene 18 años o es mayor a 18 mostrarle
    un mensaje de que puede entrar al antro.
    if statement
    > < == >= <= !=
    """
    edad_usuario = int(input("Qué edad tienes carnal? "))
    if edad_usuario >= 18:
        print("Bienvenido, disfruta el party!")
    else:
        print("Desaparecete carnal, estás morrillo!")


pedir_edad()
