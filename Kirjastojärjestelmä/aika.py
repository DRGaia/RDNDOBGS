import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def aika():

    cur.execute("SELECT id, asiakasid, kirjaid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-11 days')")

    vmuistutus = cur.fetchone()

    if vmuistutus is None:
        print("")
        print("Kenelläkään ei ole palautusaika umpeutumassa")
        print("")

    else:
        Muistutus = cur.fetchall()

        for row in Muistutus:
            print("")
            print("Lähetä muistutus näille: ", row)
            print("")

    cur.execute("SELECT id, asiakasid, kirjaid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-14 days')")

    vmyöhässä = cur.fetchone()
    if vmyöhässä is None:
        print("")
        print("Kenelläkään ei ole myöhässä palautuksia")
        print("")
    else:

        Myöhässä = cur.fetchall()

        for row in Myöhässä:
            print("")
            print("Myöhässä olevat lainaukset: ", row)
            print("")