import sqlite3
from tabulate import tabulate
from Kirjastojärjestelmä.signin import signin
conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
admin = None
asiakas = None
def logsignin():
  global admin
  global asiakas
  admin = False
  asiakas = False
  print("\nTervetuloa \n\n1) Kirjaudu sisään\n\n2) Luo käyttäjä\n")
  valinta = input()
  try:
    try:
      if valinta == "1":
        kumpi = input("\nOletko:\n\n1) Admin.\n\n2) Asiakas.\n\n")
        if kumpi == "1":
          try:
            email = input("\nAnna sähköpostiosoitteesi: \n")
            salasana = input("\nAnna salasanasi: \n")
            cur.execute("SELECT nimi FROM admin WHERE sähköpostiosoite = ? AND salasana = ? LIMIT 1", (email, salasana))
            onko = cur.fetchone()
            if onko:
              print(f"\nTervetuloa {onko[0]}")
              admin = True
            else:
              print("\nVäärä salasana tai sähköposti")
          except:
            print("\nerror\n")

        elif kumpi == "2":
          try:
            email = input("\nAnna sähköpostiosoitteesi: \n")
            salasana = input("\nAnna salasanasi: \n")
            cur.execute("SELECT nimi FROM asiakkaat WHERE sähköpostiosoite = ? AND salasana = ? LIMIT 1", (email, salasana))
            onko = cur.fetchone()
            if onko:
              print(f"\nTervetuloa {onko[0]}\n")
              asiakas = True
            else:
              print("\nVäärä salasana tai sähköposti")
          except:
            print("\nerror\n")
      elif valinta == "2":
        signin()
    except:
      pass
  except:
    pass
