import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def poisto():
    print("")
    poistovalinta = input("Haluatko poistaa (k)irjan, (a)siakkaan vai (ad)minin: ").lower()

    if poistovalinta == "a":
                print("")
                cur.execute('SELECT * FROM asiakkaat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                poistoid = input('Anna poistettavan asiakkaan id: ')
                print("")
                cur.execute("SELECT sakkosaldo FROM asiakkaat WHERE id = ?", (poistoid,))
                sak = cur.fetchone()

                if sak[0] > 0:
                    print("Et voi poistaa käyttäjää jolla on maksamattomia sakkoja \n")
                elif sak is None:
                        print("Asiakasta ei löytynyt")
                else:
                    cur.execute('DELETE FROM asiakkaat WHERE id = ?', (poistoid,))
                    conn.commit()
                    cur.execute('SELECT * FROM asiakkaat')
                    data = cur.fetchall()
                    table = tabulate(data)
                    print(table)
                    print("")
                    print("Asiakas poistettu onnistuneesti! ")
                    print("")

    elif poistovalinta == "k":
                print("")
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                poistoid = int(input('Anna poistettavan kirjan id: '))
                print("")
                cur.execute('DELETE FROM kirjat WHERE id = ?', (poistoid,))
                conn.commit()
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                print("Kirja poistettu onnistuneesti! ")
                print("")

    elif poistovalinta == "ad":
        print("")
        cur.execute('SELECT * FROM admin')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)
        print("")
        poistoid = input('Anna poistettavan adminin id: ')
        print("")
        cur.execute('DELETE FROM admin WHERE id = ?', (poistoid,))
        conn.commit()
        cur.execute('SELECT * FROM admin')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)
        print("")
        print("Admin poistettu onnistuneesti! ")
        print("")

    else:
        print("Kirjoita joko a tai k! ")

    