import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def lisäys():
    valinta = input("Haluatko lisätä (k)irjan vai (a)siakkaan: ").lower()

    if valinta == "k":
                print("")
                liskirnimi = input('Anna lisättävän kirjan nimi: ')

                print("")

                liskirkirj = input(f'Anna kirjan "{liskirnimi}" kirjoittaja: ')

                print("")

                liskirvuos = int(input(f'Anna kirjan "{liskirnimi}" julkaisuvuosi: '))

                print("")

                liskirisbn = int(input(f'Anna kirjan "{liskirnimi}" ISBN-13: '))

                print("")

                cur.execute('INSERT INTO kirjat (nimi, kirjoittaja, julkaisuvuosi, ISBN) VALUES (?, ?, ?, ?)', (liskirnimi, liskirkirj, liskirvuos, liskirisbn))
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                conn.commit()
                print(table)

    if valinta != "a" and valinta != "k":
                print("Kirjoita k tai a! ")