"""
Routing in FastAPI

Routes are crucial in FastAPI applications as they
define the endpoints clients interact with.

By creating routes, you establish the API endpoints
for communication between your application and clients.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/items/")
def read_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/")
def read_items():
    return {"users": ["users1", "users2", "users3"]}

# Path Parameters 
@app.get("/users/{users_id}")
def read_item(users_id: int):
    return {"users_id": users_id}

# Query Parameters
@app.get("/items/")
    # skip and limit
def get_items(skip: int=0, limit: int=10):
    return {"skip": skip, "limit": limit}
    #/items/?skip=3&limit=10

""" Post Request """
@app.post("/items/")
def create_item(name: str, price: float):
    return {"item_name": name, "item_price": price}

""" Put Request """
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "item_name": name, "item_price": price}

""" Delete Request """
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
