import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def aika():

    # Tarkistetaan onko jokin lainaus lähellä myöhästymistä
    cur.execute("SELECT id, asiakasid, kirjaid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-11 days')")

    muistutus = cur.fetchall()

    if not muistutus:
        print("\nKenelläkään ei ole palautusaika umpeutumassa\n")
    else:
        for row in muistutus:
            print("\nLähetä muistutus näille:", row)

    # Tarkistetaan onko jokin lainaus myöhässä
    cur.execute("SELECT id, asiakasid, kirjaid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-14 days')")

    myohassa = cur.fetchall()

    if not myohassa:
        print("\nKenelläkään ei ole myöhässä palautuksia\n")
    else:
        for row in myohassa:
            print("\nMyöhässä olevat lainaukset:", row)