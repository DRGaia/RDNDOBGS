import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

def palautus():

        cur.execute('SELECT * FROM lainaukset')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)

        if table == "":
            print("Tällä hetkellä ei lainauksia ")
            print("")
            return

        print("")

        Palatuskirja = int(input("Minkä kirjan haluat palauttaa (kirjoita lainauksen id): "))

        print("")

        # Tarkistetaan kirjan kappalemäärä
        cur.execute('SELECT id FROM lainaukset WHERE id = ?', (Palatuskirja,))
        result = cur.fetchone()

        # Lainausta jonka käyttäjä antoi ei löytynyt
        if result is None:
            print("")
            print("Lainausta ei löytynyt")
            return

        # Poistetaan lainaus
        cur.execute('DELETE FROM lainaukset WHERE id = ? ', (Palatuskirja,))

        conn.commit()

        print("")
        print("Palautus onnistui!")
        print("")