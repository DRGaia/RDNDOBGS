import sqlite3
conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def tarkistus(admin, asiakas, käyt):

    if admin == True:
        cur.execute("SELECT nimi, sähköpostiosoite, salasana  FROM admin WHERE id = ? LIMIT 1", (käyt,)) 
        tiedot = cur.fetchone()

        print(f"\nTiedot:\nNimi: {tiedot[0]}\nSähköposti: {tiedot[1]}\nSalasana: {tiedot[2]}\n")

    elif asiakas == True:
        cur.execute("SELECT nimi, syntymävuosi, sähköpostiosoite, sakkosaldo, salasana  FROM asiakkaat WHERE id = ? LIMIT 1", (käyt,)) 
        tiedot = cur.fetchone()

        print(f"\nTiedot:\nNimi: {tiedot[0]}\nSyntymävuosi: {tiedot[1]}\nSähköposti: {tiedot[2]}\nSalasana: {tiedot[4]}\nSakkosaldo: {tiedot[3]}€\n")
    input("Paina Enter nappia jatkaaksesi.")
# Antaa käyttäjä tiedot.