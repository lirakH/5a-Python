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
  return models.Movie(id=movie_id, **movie.dict())

@app.get("/movies/", response_model=List[Movie])
def read_all_movies():
  return database.read_movies()

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int):
  movie = database.read_movie(movie_id)
  if movie is None:
    raise HTTPException(status_code=404, detatil="Movie not found!")
  return movie

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie: MovieCreate):
  updated = database.update_movie(movie_id, movie)
  if not updated:
    raise HTTPException(status_code=404, detatil="Movie not found!")
  return models.Movie(id=movie_id, **movie.dict())

@app.delete("/movies/{movie_id}", response_model=dict)
def delete_movie(movie_id: int):
  deleted = database.delete_movie(movie_id)
  if not deleted:
    raise HTTPException(status_code=404, detatil="Movie not found!")
  return {"message": "Movie deleted successfully!"}
