"""
Dictionaries
{key: value}

... -3 -2 -1 0 1 2 3 ...
"""
my_list = ["hi", "hello", "hola", "bye"]
my_list.reverse()
print(my_list)


my_tuple = ("hola", "que tal", 500)
print(my_tuple)

my_address = {"name": "Pepito"}
student_address = {
    "name": "Panchito",
    "street": "4576 La Vida Loca Street",
    "city": "New York",
    "zip_code": 45546
}

juegos = {
    "name": "Need For Speed II",
    "release_year": 1999,
    "genre": ["Simulator"],
    "producer": "EA Games"
}

print(student_address["zip_code"])
print(student_address.get("country", ""))

my_dict2 = {1: "Juanito"}
print(type(my_address))
print(my_dict2)
print(student_address)
