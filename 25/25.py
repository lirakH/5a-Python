#Today we will develop a CRUD API using FastAPI that enables users to manage a collection of movies
#pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from typing import List
import database
import models
from models import Movie, MovieCreate

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Welcome to our Movie CRUD API"}
