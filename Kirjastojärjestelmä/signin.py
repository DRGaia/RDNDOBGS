import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def signin():
                print("")
                lisasinimi = input('Anna lisättävän asiakkaan nimi: ')

                print("")

                lisasivuos = int(input(f'Anna asiakkaan "{lisasinimi}" syntymävuosi: '))

                print("")

                lisasisähkö = input(f'Anna asiakkaan "{lisasinimi}" sähköposti: ')

                print("")

                lisasisaldo = int(input(f'Anna asiakkaan "{lisasinimi}" sakkosaldo: '))

                print("")

                cur.execute('INSERT INTO asiakkaat (nimi, syntymävuosi, sähköpostiosoite, sakkosaldo) VALUES (?, ?, ?, ?)', (lisasinimi, lisasivuos, lisasisähkö, lisasisaldo))
                cur.execute('SELECT * FROM asiakkaat')
                data = cur.fetchall()
                table = tabulate(data)
                conn.commit()
                print(table)