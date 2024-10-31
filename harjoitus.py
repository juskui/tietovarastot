import sqlite_con as db  # sqlite_con.py samasta hakemistosta
import pandas as pd

# import numpy as np

connection = db.conn

# sql = "select * from movies"

rows = connection.execute(  # rows type = cursor = current set of records
    "select title\
     from movies\
     where rowid > 1"
)

# viedään resultset DataFrameksi
df = pd.DataFrame(rows.fetchmany(10))

df.to_csv("top10_leffat.csv", index=True)
