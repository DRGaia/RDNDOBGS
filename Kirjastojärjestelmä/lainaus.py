import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

def lainaus():
        
        kirjat = []

        while True:
            print("")

            cur.execute('SELECT * FROM kirjat')
            data = cur.fetchall()
            table = tabulate(data)
            print(table)

            print("")

            Lainakirja = int(input("Minkä kirjan haluat lainata (kirjoita kirjan id) HUOM! Kappalemäärä: "))

            print("")

            # Päivitetään kirjalistaa, jotta usea kirja voidaan lainata, mutta ei samaa kirjaa
            if Lainakirja in kirjat:
                print("Kirja on jo valittu! ")
                continue

            # Tarkistetaan kirjan kappalemäärä
            cur.execute('SELECT kappalemäärä FROM kirjat WHERE id = ?', (Lainakirja,))
            result = cur.fetchone()

            # Kirjaa ei löytynyt
            if result is None:
                print("")
                print("Kirjaa ei löytynyt")
                return

            # result = 0 tai vähemmän -> kirja on loppu
            if result[0] <= 0:
                print("Kirja on loppu")
                continue

            kirjat.append(Lainakirja)

            lopetus = input("Lainaatko vielä (vastaa 'en' tai 'kyllä')? ")

            if lopetus == "en":
                break

        cur.execute('SELECT * FROM asiakkaat')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)

        print("")

        Lainaasiak = int(input("Kenelle haluat lainata kirjan (kirjoita asiakkaan id): "))

        print("")

        # Tarkistetaan onko asiakkaalla sakkoja
        cur.execute('SELECT sakkosaldo FROM asiakkaat WHERE id = ?', (Lainaasiak,))
        tulos = cur.fetchone()

        # Muunnetaan fetchonen antama tuple (52,) kokonaisluvuksi 52
        if tulos is not None:
             sakkosaldo = tulos[0]
        else:
             sakkosaldo = 0

        if sakkosaldo > 0:
             print(f"Asiakkaalla on {sakkosaldo} € sakkoja, joten hänelle ei voi lainata kirjoja.")
             print("")
             return

        # Tarkistetaan asiakas
        cur.execute('SELECT id FROM asiakkaat WHERE id = ?', (Lainaasiak,))
        result = cur.fetchone()

        # Asiakasta ei löytynyt
        if result is None:
            print("Asiakasta ei löytynyt")
            return
        
        # Tallennetaan laina
        for x in kirjat:
            cur.execute('UPDATE kirjat SET kappalemäärä = kappalemäärä - 1 WHERE id = ?', (x,))
            cur.execute("INSERT INTO lainaukset (kirjaid, asiakasid, pvm) VALUES (?, ?, DATE('2026-01-04'))",(x, Lainaasiak))

        conn.commit()

        print("Lainaus onnistui!")
        print("")
