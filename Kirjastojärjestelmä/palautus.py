import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

def palautus():

        print("")

        # Tulostetaan lainausten taulu selkeästi
        cur.execute("SELECT l.id, a.nimi AS asiakas, k.nimi AS kirja, l.pvm FROM lainaukset l JOIN asiakkaat a ON l.asiakasid = a.id JOIN kirjat k ON l.kirjaid = k.id")

        data = cur.fetchall()
        headers = [desc[0] for desc in cur.description]

        from tabulate import tabulate
        print(tabulate(data, headers=headers, tablefmt="grid"))

        if headers == "":
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
            print("Lainausta ei löytynyt")
            print("")
            return

        # Poistetaan lainaus
        cur.execute('DELETE FROM lainaukset WHERE id = ? ', (Palatuskirja,))

        # Otetaan oikea id, jotta oikean kirjan määrää voidaan lisätä
        kirjaid = result[0]

        # lisätään kappalemäärä palautettuun kirjaan
        cur.execute('UPDATE kirjat SET kappalemäärä = kappalemäärä + 1 WHERE id = ?', (kirjaid,))

        conn.commit()

        print("")
        print("Palautus onnistui!")
        print("")