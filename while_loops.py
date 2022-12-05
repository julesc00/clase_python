"""
while loop = mientras (tal condición sea o no sea)
infinite loop
"""


def sum_to_50():
    total, trigger = 0, False
    number1 = int(input("Ingrese un número: "))
    number2 = int(input("Ingrese otro número: "))
    total = number1 + number2
    while not trigger:
        msg1 = input("Va a agregar otro número? escriba 'y' para sí y 'n' para no: ")
        if msg1 == "y":
            num = int(input("Ingrese un número: "))
            total += num
            print(f"Total: {total}")
        else:
            trigger = True
    return f"Total: {total}"


print(sum_to_50())


def x():
    return ["hello" if i == "yes" else "no" for i in range(0, 10)]
