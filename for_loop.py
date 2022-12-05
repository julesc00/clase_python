
NAMES = [
    "Panchito",
    "Petra",
    "Juan",
    "Pita",
    "Michael"
]

PETS = [
    "Cat",
    "Dog",
    "Parrot",
    "Hamster"
]

NUMBERS = [1, 2, 3]


def list_items(items):
    print(items)

    for item in items:
        print(f"{item}s")

    for number in items:
        number += 1
        print(number)


list_items(NUMBERS)


def find_name(names):
    for name in names:
        if name == "Petra":
            print(f"{name} sí es!!!")
        else:
            print("Petra no es :(")


def check_if_name_in_list(name, names):
    if name in names:
        print(f"{name} sí está")
    else:
        print(f"{name} no está")


check_if_name_in_list("Jose", NAMES)
print("*" * 20)
find_name(NAMES)
print("*" * 40)

"""
1. Página con formulario que registra los usuarios (Frontend).
2. El backend recibe una lista con los logins de los usuario. (Backend)
3. Crear una función: list_students(), que arroje el total de usuarios, más la lista de los logins. (Backend) 
4. Vincular la función con el componente del frontend que lo muestre en una lista ordenada. (Frontend)
"""
USERS = ["panchito09", "jedi2022", "el_bañado"]


def list_users(users):

    name = "Julio"
    # borrar el último usuario
    users.pop()
    print(len(name))
    counter = len(users)  # length
    print(f"El total de usuarios es: {counter}")
    return {
        "total_users": counter,
        "users": sorted(users)
    }


print(list_users(USERS))
