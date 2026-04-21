import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

def lainaus():
    
        print("")

        cur.execute('SELECT * FROM kirjat')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)

        Lainakirja = int(input("Minkä kirjan haluat lainata (kirjoita kirjan id) HUOM! Kappalemäärä: "))

        print("")

        # Tarkistetaan kirjan kappalemäärä
        cur.execute('SELECT kappalemäärä FROM kirjat WHERE id = ?', (Lainakirja,))
        result = cur.fetchone()

        # Kirjaa ei löytynyt
        if result is None:
            print("")
            print("Kirjaa ei löytynyt")
            return
        
        kappalemäärä = result[0]

        # Kirja on loppu
        if kappalemäärä <= 0:
            print("")
            print("Kirja on loppu")
            return

        cur.execute('SELECT * FROM asiakkaat')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)

        print("")

        Lainaasiak = int(input("Kenelle haluat lainata kirjan (kirjoita asiakkaan id): "))

        print("")

        # Tarkistetaan asiakas
        cur.execute('SELECT id FROM asiakkaat WHERE id = ?', (Lainaasiak,))
        result = cur.fetchone()

        # Asiakasta ei löytynyt
        if result is None:
            print("Asiakasta ei löytynyt")
            return
        
        # Tallennetaan laina
        cur.execute('INSERT INTO lainaukset (kirjaid, asiakasid, pvm) VALUES (?, ?, DATE("now"))', (Lainakirja, Lainaasiak))

        # Muokataan kappalemäärä
        cur.execute('UPDATE kirjat SET kappalemäärä = kappalemäärä - 1 WHERE id = ? ', (Lainakirja,))

        conn.commit()

        print("")
        print("Lainaus onnistui!")