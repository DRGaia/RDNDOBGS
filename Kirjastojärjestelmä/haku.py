import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def haku():
    print("")
    Ekirja = input("Mitä kirjaa etsit (kirjoita kirjan nimi tai kirjailija): ")

    print("")

    # Hakee tietokannasta kirjaa tai kirjailijaa, joka vastaa Ekirja-muuttujaa
    Tulokset = cur.execute("SELECT * FROM kirjat WHERE nimi LIKE ? OR kirjoittaja LIKE ?",('%' + Ekirja + '%', '%' + Ekirja + '%')).fetchall()

    if not Tulokset:
        print("Kirjaa ei löytynyt. ")
        
    # Haun pitää olla vähintään 6 merkkiä
    elif len(Ekirja) < 6:
        print("Anna selvempi haku. ")

    else:
        for kirja in Tulokset:
            print(kirja)