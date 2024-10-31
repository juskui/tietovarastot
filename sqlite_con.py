import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect("./databases/movies.db")
except Error as e:
    print(e)

print(None)
