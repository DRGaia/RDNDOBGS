import sqlite3
from tabulate import tabulate
conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def historia():
        
        print("")

        cur.execute('SELECT * FROM asiakkaat')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)
        
        print("")

        asiakasvalinta = input("Kenen asiakkaan tiedot näytetään (anna id): ")

        cur.execute("SELECT nimi, sähköpostiosoite, salasana FROM asiakkaat WHERE id = ? LIMIT 1", (asiakasvalinta,)) 
        tiedot = cur.fetchone()

        print(f"\nTiedot:\nNimi: {tiedot[0]}\nSähköposti: {tiedot[1]}\nSalasana: {tiedot[2]}\n")

        # Tulostetaan taulu tietyn asiakkaan lainauksista järkevästi (ei: 1, 2, 3, 2026-04-09)
        cur.execute("SELECT l.id, a.nimi AS asiakas, k.nimi AS kirja, l.pvm FROM lainaukset l JOIN asiakkaat a ON l.asiakasid = a.id JOIN kirjat k ON l.kirjaid = k.id WHERE a.id = ?", (asiakasvalinta,))
        data = cur.fetchall()

        headers = [desc[0] for desc in cur.description]

        print(tabulate(data, headers = headers, tablefmt="grid"))

        print("")

        # Jos taulu on tyhjä
        if not data:
            print("")
            print("Tällä hetkellä ei lainauksia ")
            print("")
            return