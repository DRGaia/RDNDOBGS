import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def poisto():
    poistovalinta = input("Haluatko poistaa (k)irjan, (a)siakkaan vai (ad)minin: ").lower()

    if poistovalinta == "a":
                print("")
                cur.execute('SELECT * FROM asiakkaat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                poistoid = input('Anna poistettavan asiakkaan sähköpostiosoite: ')
                print("")
                cur.execute("SELECT sakkosaldo FROM asiakkaat WHERE sähköpostiosoite = ?", (poistoid,))
                sak = cur.fetchone()

                if sak[0] > 0:
                    print("et voi poistaa käyttäjää joilla on sakkoja maksamatta\n")
                elif sak is None:
                        print("asiakasta ei löytynyt")
                else:
                    cur.execute('DELETE FROM asiakkaat WHERE sähköpostiosoite = ?', (poistoid,))
                    conn.commit()
                    cur.execute('SELECT * FROM asiakkaat')
                    data = cur.fetchall()
                    table = tabulate(data)
                    print(table)

    elif poistovalinta == "k":
                print("")
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)
                print("")
                poistoid = int(input('Anna poistettavan kirjan ID: '))
                print("")
                cur.execute('DELETE FROM kirjat WHERE id = ?', (poistoid,))
                conn.commit()
                cur.execute('SELECT * FROM kirjat')
                data = cur.fetchall()
                table = tabulate(data)
                print(table)

    elif poistovalinta == "ad":
        print("")
        cur.execute('SELECT * FROM admin')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)
        print("")
        poistoid = input('Anna poistettavan adminin sähköpostiosoite: ')
        print("")
        cur.execute('DELETE FROM admin WHERE sähköpostiosoite = ?', (poistoid,))
        conn.commit()
        cur.execute('SELECT * FROM admin')
        data = cur.fetchall()
        table = tabulate(data)
        print(table)

    else:
                print("Kirjoita joko a tai k! ")

    