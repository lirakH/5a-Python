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

#CRUD(api comands) - Create(post) Read(get) Update(put) Delete(delete)
@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate):
  movie_id = database.create_movie(movie)
