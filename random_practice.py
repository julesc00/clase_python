import random


def generate_random_number():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print(f"""
        Number 1 is: {number1}
        Number 2 is: {number2}
    """)
    return number1 + number2


def generate_random_range():
    number = random.randrange(0, 100, 5)
    return number


def generate_random_color():
    color = random.choice(["red", "black", "green", "yellow", "pink", "purple", "white"])
    return color


# print(generate_random_number())
# print(generate_random_range())
print(generate_random_color())
