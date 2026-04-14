import sqlite3
from tabulate import tabulate
conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()

print("Tervetuloa \n\n1) Kirjaudu sisään\n\n2) Luo käyttäjä\n")
valinta = input()
try:
  try:
    if valinta == "1":
      kumpi = input("\nOletko:\n\n1) Admin.\n\n2) Asiakas.\n")
      if kumpi == "1":
        try:
          email = input("Anna sähköpostiosoitteesi: ")
          salasana = input("Anna salasanasi: ")
          cur.execute("SELECT nimi FROM admin WHERE sähköpostiosoite = ? AND salasana = ? LIMIT 1", (email, salasana))
          onko = cur.fetchone()
          if onko:
            print(f"Tervetuloa {onko[0]}")
          else:
            print("Väärä salasana tai sähköposti")
        except:
          print("error")

    if kumpi == "2":
        try:
          email = input("Anna sähköpostiosoitteesi: ")
          salasana = input("Anna salasanasi: ")
          cur.execute("SELECT nimi FROM asiakkaat WHERE sähköpostiosoite = ? AND salasana = ? LIMIT 1", (email, salasana))
          onko = cur.fetchone()
          if onko:
            print(f"Tervetuloa {onko[0]}")
          else:
            print("Väärä salasana tai sähköposti")
        except:
          print("error")
  except:
    pass
except:
  pass
