"""

Introduction to SQLite 

SQLite is a C-language library that provides a lightweight, disk-based database.
It reads and writes directly to ordinary disk files, making it a self-contained and zero-configuration database engine. 
SQLite is often favored for its portability and the fact that it does not require any setup or administration, which 
is beneficial for applications where a full-fledged database server would be overkill.

SQLite Architecture 
It stores the entire database, including definitions, tables, indices, and the data itself, in a single cross-platform file on the host machine.

Advantages 
- lightweight 
- no setup or administration
- portability
- self-contained

Disadvantages 
- not designed for high-concurrency applications
- unsuitable for web applications

How to Install
- https://www.sqlite.org/download.html
  (Precompiled Binaries for Windows)
- https://www.sqlite.org/2025/sqlite-tools-win-x64-3500200.zip 
- download
- Create a folder in C:
- Extract the zip to that folder

Extra after Install:
- .open mydatabase.db
  (opens the db or creates one with this name if we don't have it)
- CREATE TABLE users ( 
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL 
  );
- INSERT INTO users (name, email) VALUES ('deti', 'troll@gmail.com');
- SELECT * FROM users;
- UPDATE users SET email = 'newtroll@gmail.com' WHERE id=1;
- DELETE FROM users WHERE id=1;




