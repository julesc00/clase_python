# Functions

def action_definition():
    pass


students_list = []


def add_name(student_name):
    name = student_name.title()
    return name


def add_arguments(*args):
    pass


def add_lastname(name, last_name):
    name = add_name(name)
    fullname = f"{name} {last_name.title()}"
    return fullname


def get_age(number):
    if number < 18:
        return "Eres menor de edad, tírate a perder."
    else:
        return number


def add_to_member(age):
    members = []
    user_age = get_age(age)
    members.append(user_age)


def get_birth_year(age, current_year):
    birth_year = current_year - age
    return birth_year


def get_birth_year2(current_percentage):
    porcentaje = current_percentage
    age = 20
    current_year = 2022
    return current_year - age


add_lastname("Jemima", "Briones")
print(f"Franz-che nació en el año {get_birth_year(20, 2022)}")
