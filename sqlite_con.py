# import sqlite3
# from sqlite3 import Error

# try:
#     conn = sqlite3.connect("./databases/movies.db")
# except Error as e:
#     print(e)

import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("./databases/movies.db") as conn:
        pass  # Your database operations go here
except Error as e:
    print(e)
