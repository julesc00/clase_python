
# Slicing
def msg_formatter():
    my_message = "hello there Michele!"
    name = my_message[12:-1]
    names = [name]
    print(names)
    print(name)
    new_message = "".join(f"{my_message} {name}")
    print(new_message)


def access_items():
    # string[start, stop, step]
    my_nums2 = [i for i in range(1, 100+1)]
    print(my_nums2)
    print(my_nums2[::2])


def select_items():
    my_list = ["one", "two", "three", "four"]
    print(my_list[1:3])


def reverse_items():
    my_tuple = (1, 2, 3, 4, 5)
    my_reversed_tuple = my_tuple[::-1]
    print(my_reversed_tuple)


if __name__ == "__main__":
    msg_formatter()
    access_items()
    reverse_items()
    select_items()
