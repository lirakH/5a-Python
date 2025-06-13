from fastapi import FastAPI

# no type hints
def format_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(format_name("lirak","hamiti"))

#with type hints
def get_full_name(first_name: str, last_name: str, age: int):
    full_name = first_name.title() + " " + last_name.title() + " " + str(age)
    return full_name
print(get_full_name("lirak","hamiti",100))


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

print(get_items("apple", 42, 3.14, True, b"data"))
