import sqlite_con as db  # sqlite_con.py samasta hakemistosta
import pandas as pd
from pathlib import Path

# tee tyhjä tiedosto samaan hakemistoon
Path("leffat.db").touch()

# kantayhteys
connection = db.conn

# kursori
cursor = connection.cursor()

cursor.execute(
    "create table if not exists movies\
          (id int, \
          title text,\
          overview text,\
          release_date text,\
          vote_average real,\
          vote_count int)"
)

# ladataan kursorin data pandas DataFrameen
moviedata = pd.read_csv("titles-3.csv")

# tallennetaan sqlite tauluun
# tauku      #yhteys    #jos taulu on jo mitä tehdään #ei tuoda indexiä
moviedata.to_sql("moviess", connection, if_exists="append", index=False)
