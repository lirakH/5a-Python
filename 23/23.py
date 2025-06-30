"""
Advanced Type Annotations and Integrating Tools 

Advanced type annotations in Python provide a strong way to specify the expected types of variables, function parameters, and return values.

They enhance code readability and maintainability, especially in larger codebases, by making the data flow and function contracts explicit.

Some key advanced type annotations include Optional, Union, and Any.

The `Optional` type is used when a variable or function parameter can be of a specified type or `None`.
The Union type is used to indicate that a variable or parameter can be one of several specified types.
The Any type is used when a variable can be of any type.

"""
from typing import Optional, Any, Union, List

def get_name(name: Optional[str] = None) -> str:
  if name:
    return name
  return "Anonymous"

print(get_name())
print(get_name("Lirak"))
print(get_name(12))

def process_value(value: Union[int, str]) -> str:
  if isinstance(value, int):
    return f"Number: {value}"
  return f"String: {value}"

# print(process_value())
print(process_value("Lirak"))
print(process_value(12))

def process_anything(value: Any) -> str:
  tipi = type(value)
  return f"Processed {type}: {value}"

# print(process_anything())
print(process_anything("Lirak"))
print(process_anything(12))
print(process_anything([12,3,"a",9]))

def sum_of_numbers(numbers: List[int]) -> int:
  return sum(numbers)

numbers: List[int] = [1,2,3]
result: int = sum_of_numbers(numbers)
print(result)









