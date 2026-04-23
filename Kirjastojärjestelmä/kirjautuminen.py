import sqlite3
from tabulate import tabulate
from Kirjastojärjestelmä.signin import signin
conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
admin = None
asiakas = None
käyt = None
def logsignin():
  global admin # nää on vaa ne jotka siirretään toisiin tiedostoihin kuten main
  global asiakas
  global käyt
  admin = False
  asiakas = False
  print("\nTervetuloa \n\n1) Kirjaudu sisään\n\n2) Luo käyttäjä\n")
  valinta = input()
  try:
    try:
      if valinta == "1": # onko asiakas admin vai asiakas
        kumpi = input("\nOletko:\n\n1) Admin.\n\n2) Asiakas.\n\n")
        if kumpi == "1":
          try:
            email = input("\nAnna sähköpostiosoitteesi: \n")
            salasana = input("\nAnna salasanasi: \n")
            cur.execute("SELECT id, nimi FROM admin WHERE sähköpostiosoite = ? AND salasana = ? LIMIT 1", (email, salasana)) #varmistaa käyttäjä sähköpostin ja salasanan ja antaa takas id ja nimen
            onko = cur.fetchone()
            if onko:
              print(f"\nTervetuloa {onko[1]}\n")
              admin = True
              käyt = onko[0] # käytetään rakistus.py:ssä
            else:
              print("\nVäärä salasana tai sähköposti")
          except:
            print("\nerror\n")

        elif kumpi == "2":
          try:
            email = input("\nAnna sähköpostiosoitteesi: \n")
            salasana = input("\nAnna salasanasi: \n")
            cur.execute("SELECT id, nimi FROM asiakkaat WHERE sähköpostiosoite = ? AND salasana = ? LIMIT 1", (email, salasana))
            onko = cur.fetchone()
            if onko:
              print(f"\nTervetuloa {onko[1]}\n")
              käyt = onko[0]
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