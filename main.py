import sqlite_con as db  # sqlite_con.py samasta hakemistosta
import pandas as pd
import csv

# import numpy as np

connection = db.conn

# sql = "select * from movies"

rows = connection.execute(  # rows type = cursor = current set of records
    "select title\
     from movies\
     where title like 'A%'\
    "
)

# with open("titles-csv.csv", "w", newline="") as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow([i[0] for i in rows.description])  # write headers
#     csvwriter.writerows(rows.fetchall())

# viedään resultset DataFrameksi
df = pd.DataFrame(rows.fetchall())
print(df)

# tallennetaan csv-tiedostoon
df = pd.read_sql("Select * from movies", connection)
df.to_csv("titles-3.csv", index=True)

# tallennetaan json:ksi
df.to_json("titles.json", index=True)

# tallenna listaan
lista = []
for row in rows:
    lista.append(row)
print(lista)


with open("leffat.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(lista)

# for row in rows:
#     print(row)

# a = rows.fetchone()
# print((a))

# haetaan seuraava tulos
# iteraattori = iter(rows)
# rivi = next(iteraattori)  # next siirtyy indexissä yhdellä eteenpäin
# rivi2 = next(iteraattori)

# print(rivi, rivi2)

# connection.close()
