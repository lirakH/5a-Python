"""
models

In Pydantic, a model is akin to a data class but comes with powerful validation and parsing capabilities. 
Pydantic models are defined using Python's type annotations, and they automatically validate the data assigned to them. 

Pydantic models are like blueprints for your data in Python. Imagine you're building a house, and you need a plan to make 
sure everything fits perfectly. Pydantic helps you create a plan for your data. 

"""
from pydantic import BaseModel, FieldValidationInfo, field_validator, constr, conint
from typing import Optional

class User(BaseModel):
  id: int
  name: str
  age: Optional[int] = 15
  email: Optional[str] = None

user1 = User(id=1, name="John Doe", age=15, email="john@gmail.com")
user2 = User(id=2, name="Filan Fisteku", email="filan2002@gmail.com")

print(user1)
print(user2)
