import sqlite3
from models import Movie, MovieCreate

def create_connection():
  #create a connection to the SQLite database
  con = sqlite3.connect("movies.db")
  con.row_factory = sqlite3.Row
  return con
  
"""
cursor.fetchall() informatat do dalin si kjo:
  (
  (1,"Cobra Kai tv", "Jon Hurwitz, Hayden Schlossberg, and Josh Heald"),
  (2,"Finding Nemo", "Andrew Ayers Stanton")
  )
  
fetchone() informatat do dalin si kjo:
  (1,"Cobra Kai tv", "Jon Hurwitz, Hayden Schlossberg, and Josh Heald"),

row_factory informatat do dalin si kjo:
  row[0]  # 1
  row[1]  # 'Cobra Kai tv'
  row[2]  # 'Jon Hurwitz, Hayden Schlossberg, and Josh Heald'

sqlite3.Row informatat do dalin si dictionary:
  ("id":1, "title":"Cobra Kai tv", "director":"Jon Hurwitz, Hayden Schlossberg, and Josh Heald")
  row['title'] #Cobra Kai tv
"""

def create_table():
  con = create_connection():
  cursor = con.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      director TEXT NOT NULL
      )
      """
  )
  con.commit()
  con.close()

create_table()

def create_movie(movie: MovieCreate) -> int:
  """
    Adds a new movie to the database.
    
    Args:
        movie (MovieCreate): A pydantic model containing the title and director of the movie to be created.
    
    Returns:
        int: The ID of the newly created movie in the database.
  """
  con = create_connection()
  cursor = con.cursor()
  cursor.execute("INSERT INTO movies (title, director) VALUES (?,?)", (movie.title, movie.director))
  con.commit()
  con.close()
  return movie_id

def read_movies():
  """
    Retrieves all movies from the database.
    
    Returns:
        list: A list of Movie models representing all movies in the database.
  """
  con = create_connection()
  cursor = con.cursor()
  cursor.execute("SELECT * FROM movies")
  rows = cursor.fetchall()
  con.close()
  movies = [Movie(id=row[0], title=row[1], director=row[2]) for row in rows]
  return movies

def read_movie(move_id: int):
  """
    Retrieves a single movie from the database by its ID.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        Movie: A Movie model representing the retrieved movie.
        Returns None if the movie is not found.
    """
  con = create_connection()
  cursor = con.cursor()
  cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
  rows = cursor.fetchone()
  con.close()
  if row is None:
    return None
  movie = Movie(id=row[0], title=row[1], director=row[2])
  return movie


def update_movie(movie_id: int, movie: MovieCreate) -> bool:
  """
    Updates an existing movie in the database.
    
    Args:
        movie_id (int): The ID of the movie to update.
        movie (MovieCreate): A pydantic model containing the new title and director of the movie.
    
    Returns:
        bool: True if the movie was updated successfully, False otherwise.
  """
  con = create_connection()
  cursor = con.cursor()
  cursor.execute("UPDATE movies SET title = ?, director = ? WHERE id = ?", (movie.title, movie.director, movie_id))
  con.commit()
  updated = cursor.rowcount
  con.close()
  return updated > 0

def delete_movie(movie_id: int) -> bool:
  """
    Deletes a movie from the database by its ID.
    
    Args:
        movie_id (int): The ID of the movie to delete.
    
    Returns:
        bool: True if the movie was deleted successfully, False otherwise.
  """
  con = create_connection()
  cursor = con.cursor()
  cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
  con.commit()
  deleted = cursor.rowcount
  con.close()
  return deleted > 0
  



