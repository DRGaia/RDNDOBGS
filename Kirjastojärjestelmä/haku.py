import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def haku():
    Ekirja = input("Mitä kirjaa etsit (kirjoita kirjan nimi tai kirjailija): ")

    Tulokset = cur.execute("SELECT * FROM kirjat WHERE nimi LIKE ? OR kirjoittaja LIKE ?",('%' + Ekirja + '%', '%' + Ekirja + '%')).fetchall()

    if not Tulokset:
        print("Kirjaa ei löytynyt.")
        
    elif len(Ekirja) < 6:
        print("Kirjoita kokonimi. ")

    else:
        for kirja in Tulokset:
            print(kirja)