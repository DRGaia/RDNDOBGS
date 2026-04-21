import sqlite3
from tabulate import tabulate
from datetime import datetime

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def aika():

    cur.execute("SELECT id, asiakasid, kirjaid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-11 days')")

    vmuistutus = cur.fetchone()

    if vmuistutus is None:
        print("Kenelläkään ei ole palautus aika umpeutumassa")

    else:
        Muistutus = cur.fetchall()

        for row in Muistutus:
            print("Lähetä muistutus näille: ", row)

    
    cur.execute("SELECT id, asiakasid, kirjaid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-14 days')")

    vmyöhässä = cur.fetchone()
    if vmyöhässä is None:
        print("Kenelläkään ei ole myöhässä palautuksia")

    else:

        Myöhässä = cur.fetchall()

        for row in Myöhässä:
            print("Myöhässä olevat lainaukset: ", row)
        