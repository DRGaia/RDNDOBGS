import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()


def sakko():

    print("")

    cur.execute("SELECT asiakasid, pvm FROM lainaukset WHERE DATE(pvm) < DATE('now', '-14 days')")

    myöhässä = cur.fetchall()

    for asiakasid, pvm in myöhässä:

        # laske myöhästyneet päivät
        cur.execute("SELECT JULIANDAY('now') - JULIANDAY(?) - 14", (pvm,))
        
        päivät = cur.fetchone()[0]

        if päivät > 0:
            sakko = int(päivät)

            cur.execute("UPDATE asiakkaat SET sakkosaldo = sakkosaldo + ? WHERE id = ?", (sakko, asiakasid))

            conn.commit()

            print("sakot päivitetty", sakko)