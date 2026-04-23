import sqlite3
conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def muokkaus(admin, asiakas, käyt):

    if admin == True:

        print("")
        nimenmuokkaus = input("Kirjoita nimi jonka haluat: ")
        print("")
        postinmuokkaus = input("Kirjoita sähköpostiosoite jonka haluat: ")
        print("")

        # Muokataan käyttäjän antamat tiedot tietokannassa
        cur.execute("UPDATE admin SET nimi = ?, sähköpostiosoite = ? WHERE id = ?", (nimenmuokkaus, postinmuokkaus, käyt))

        # Päivitetään tiedot tietokantaan
        conn.commit()

        # Tulostetaan päivitetyt tiedot
        cur.execute("SELECT nimi, sähköpostiosoite, salasana FROM admin WHERE id=?", (käyt,))
        tiedot = cur.fetchone()

        print(f"\nTiedot:\nNimi: {tiedot[0]}\nSähköposti: {tiedot[1]}\nSalasana: {tiedot[2]}\n")

    elif asiakas == True:
                
        print("")
        nimenmuokkaus = input("Kirjoita nimi jonka haluat: ")
        print("")
        postinmuokkaus = input("Kirjoita sähköpostiosoite jonka haluat: ")
        print("")

        # Muokataan käyttäjän antamat tiedot tietokannassa
        cur.execute("UPDATE asiakkaat SET nimi = ?, sähköpostiosoite = ? WHERE id = ?", (nimenmuokkaus, postinmuokkaus, käyt))

        # Päivitetään tiedot tietokantaan
        conn.commit()

        # Tulostetaan päivitetyt tiedot
        cur.execute("SELECT nimi, sähköpostiosoite, salasana FROM asiakkaat WHERE id=?", (käyt,))
        tiedot = cur.fetchone()

        print(f"\nTiedot:\nNimi: {tiedot[0]}\nSähköposti: {tiedot[1]}\nSalasana: {tiedot[2]}\n")