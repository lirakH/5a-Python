#The sqlite3 library in Python provides a simple and efficient way to interact with SQLite databases.
import sqlite3

# connect our file/app with the database (or create db if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students ( 
    student_id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL 
  )
  ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses ( 
    course_id INTEGER PRIMARY KEY, 
    course_name TEXT NOT NULL, 
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
  )
  ''')

cursor.execute("INSERT INTO students (name, email) VALUES ('?', '?');", ("filan", "filan@gmail"))
cursor.execute("INSERT INTO students (name, email) VALUES ('fisteku', 'fisteku@gmail.com');")

cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Math', 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Fizike', 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES ('Art', 2)")

conn.commit()

# Execute a JOIN query to combine data from students and courses
cursor.execute('''
  SELECT students.name, courses.course_name
  FROM students
  JOIN courses ON students.student_id = courses.student_id
''')

# Fetch and display the results
rows = cursor.fetchall()
for row in rows:
  print(f"Studenti: {row[0]}, Course: {row[1]}")
  
conn.close()


