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
  age: Optional[int]     #Optional Fields
  email: Optional[str] = None #Default Values (None)
  address: Optional[str] = "Ferizaj" #Default Values (Ferizaj)

user1 = User(id=1, name="John Doe", age=15, email="john@gmail.com", address="Prishtina")
user2 = User(id=2, name="Filan Fisteku", age=100, email="filan2002@gmail.com")

print(user1)
print(user2)

#Field Constraints 
class another_user(BaseModel):
  id: conint(gt=0) #id must be greater than 0
  name: constr(min_length=2, max_length=20) # name length must be between 2 and 20

valid_user = another_user(id=1, name="Shkolla")
print(valid_user)

