import sqlite3

con = sqlite3.connect("hambi.db")
print("Adatbázis létrehozva")

con.execute(
    "create table hambi (id INTEGER PRIMARY KEY AUTOINCREMENT, nev TEXT NOT NULL, husi TEXT UNIQUE NOT NULL,suly TEXT NOT NULL, ar TEXT NOT NULL, daarabszam TEXT NOT NULL)")

print("Adatbázis sikeresen létrehozva")

con.close()
