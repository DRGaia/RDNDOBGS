import sqlite3
import mysql.connector
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def poisto():
    poistovalinta = input("Haluatko poistaa (k)irjan vai (a)siakkaan: ").lower()

    if poistovalinta == "a":
                print("")
                cur.execute('SELECT * FROM asiakkaat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                poistomail = input('Anna poistettavan asiakkaan sähköpostiosoite: ')
                print("")
                cur.execute('DELETE FROM asiakkaat WHERE sähköpostiosoite = ?', (poistomail,))
                conn.commit()
                cur.execute('SELECT * FROM asiakkaat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)

    elif poistovalinta == "k":
                print("")
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                poistoisbn = int(input('Anna poistettavan kirjan ISBN: '))
                print("")
                cur.execute('DELETE FROM kirjat WHERE ISBN = ?', (poistoisbn,))
                conn.commit()
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)

    else:
                print("Kirjoita joko a tai k! ")