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

            # Muokataan kappalemäärä
            cur.execute('UPDATE kirjat SET kappalemäärä = kappalemäärä - 1 WHERE id = ? ', (Lainakirja,))

            # Päivitetään kirjalistaa, jotta usea kirja voidaan lainata, mutta ei samaa kirjaa
            if Lainakirja not in kirjat:
                kirjat.append(Lainakirja)
            else:
                print("Kirja on jo valittu")
                print("")

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

        # Tarkistetaan asiakas
        cur.execute('SELECT id FROM asiakkaat WHERE id = ?', (Lainaasiak,))
        result = cur.fetchone()

        # Asiakasta ei löytynyt
        if result is None:
            print("Asiakasta ei löytynyt")
            return
        
        # Tallennetaan laina
        for x in kirjat:
            cur.execute('INSERT INTO lainaukset (kirjaid, asiakasid, pvm) VALUES (?, ?, DATE("now"))', (x, Lainaasiak))

        conn.commit()

        print("")
        print("Lainaus onnistui!")
        print("")