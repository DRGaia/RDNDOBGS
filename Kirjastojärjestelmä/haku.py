import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def haku():
    print("")
    Ekirja = input("Mitä kirjaa etsit (kirjoita kirjan nimi tai kirjailija): ")
    print("")

    # Etsii kirjaa vertailemalla hakusanaa ja kirjan tai kirjoittajan nimeä      kirjan nimi pitää olla alusta, mutta kirjoittajan nimi voi olla mistä vain
    Tulokset = cur.execute("SELECT * FROM kirjat WHERE nimi LIKE ? OR kirjoittaja LIKE ?",(Ekirja + '%', '%' + Ekirja + '%')).fetchall()

    if not Tulokset:
        print("Kirjaa tai kirjoittajaa ei löytynyt.")
        print("")

    else:
        for kirja in Tulokset:
            print(kirja)
            print("")