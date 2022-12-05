from math import floor
import array

# # Variables
#
# # strings - cadena - texto
# candy = "chocolate"
# # PEP8
#
# # Snakecase
# sour_candy = "picafresa"
# too_sweet_candy = "cajeta"
# account_number = "a3julio#/95"
# name = "Oscar"
# car = "This is Oscar's car."
# var = 'something'
#
# print(candy, too_sweet_candy)
# print(car)
# print(account_number)
#
# # Integers - enteros
# sub_total = 1_000
# extra = 100
# extra_total = extra + extra
# tax = 200
# total = (sub_total+extra_total) - tax
# print(total)


# hard-code
# fruit = "orange"
# print(fruit)
# print(fruit.capitalize())
# fruit_uppercase = fruit.upper()
# print(fruit_uppercase)
# fruit_lowercase = fruit_uppercase.lower()
# print(fruit_lowercase)
#
# user_name = input("Ponga su nombre: ").capitalize()
# user_lastname = input("Ahora ponga sus apellidos: ").title()
# print(f"Usted se llama1: {user_name} {user_lastname} {2}.")
# print("Usted se llama1.1: {} {} {}".format(user_name, user_lastname, 2))
# print("Usted se llama2:", user_name, user_lastname, 2)
# print("Usted se llama3: " + user_name + user_lastname + str())

# Arithmetic
# medidas = 45 * 25
# # restar
# year_of_birth = 2005
# year_of_contract = 2022
# difference = year_of_contract - year_of_birth
# print("Difference:", difference, "years")
#
# # decimales = float()
# print(float(25))
# print(round(22.7))
# print(floor(22.7))
#
# # Booleans
# yes = True
# No = False
#
# # divide /
# print(25 / 3)
#
# # Data structures
# # listas
my_list = [1, "uno", True, False, [2, 3, 4, 5], {"name": "panchito"}, ("hola", "que tal")]
# my_array = [1, 2, 3, 4, 5]
# print(type(my_array))
# print(my_list)

# Booleans - Buleanos
# True = sí
# False = no


def turn_on_off_light():
    trigger = True
    if trigger == True:
        print()


def prender_apagar_luz():
    apagador = True
    if apagador == True:
        print("Apague la luz")
        apagador = False
    else:
        print("Prenda la luz")
        apagador = True
    print(f"El apagador tiene: {apagador}")


prender_apagar_luz()


# Lists vs Tuples vs Sets
"""
Lists: mutables, que se pueden modificar, al agregar o quitar, o editar.
Tuples: inmutables, una vez creados, no se modifican.
Sets: mutables, no admiten duplicados.
"""
students_list = [
    "panchito",
    "Alex",
    "Jimena"
]
my_tuple = (
    "hello",
    1,
    True,
    ("me",)
)
my_tuple2 = ("hello",)
my_set = {"hello", "hello"}
print(my_set)


def controlar_lista_de_estudiantes():
    students = []
    name1 = "Jorge"
    name2 = "Jose"
    # .append() agregar un objeto
    students.append(name1)
    students.append(name2)
    print(students)

    # .pop() quita el último objeto
    students.pop()
    return students


print(controlar_lista_de_estudiantes())


