from fastapi import FastAPI

# Create an instance of the FastAPI class
app =  FastAPI()

# Define a route for the root URL ("/") using the HTTP GET method
@app.get("/")
def root():
    # Return a dictionary with a single key-value pair as JSON response
    return {"message":"Hello world!"}

"""
Uvicorn main:app --reload 

(name of the file “main” and name of the app “app”,
and we can use –reload flag to make the server automatically
refresh anytime you make changes to the file.):
"""

# Define a route that accepts a query parameter
@app.get("/greet/")
def read_root(name: str):
    return {"message": f"Hello, {name}!"}
