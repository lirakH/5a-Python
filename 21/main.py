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

@app.get("/users/{users_id}")
def read_item(users_id: int):
    return {"users_id": users_id}



