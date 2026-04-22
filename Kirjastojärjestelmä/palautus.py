import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

def palautus():

        print("")

        cur.execute("""
        SELECT 
            a.nimi AS asiakas,
            GROUP_CONCAT(k.nimi, ', ') AS kirjat
        FROM lainaukset l
        JOIN asiakkaat a ON l.asiakasid = a.id
        JOIN kirjat k ON l.kirjaid = k.id
        GROUP BY a.id
        """)

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
            print("")
            print("Lainausta ei löytynyt")
            return

        # Poistetaan lainaus
        cur.execute('DELETE FROM lainaukset WHERE id = ? ', (Palatuskirja,))

        conn.commit()

        print("")
        print("Palautus onnistui!")
        print("")