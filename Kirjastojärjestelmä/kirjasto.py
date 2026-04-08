import sqlite3
import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root", 
  password="",
  use_pure=True
)

print("Tervetuloa \n\n1) Kirjaudu sisään\n\n2) Luo käyttäjä\n")
valinta = input()
try:
  try:
    if valinta == "1":
      kumpi = input("\nOletko:\n\n1) Admin.\n\n2) Asiakas.\n")
      if kumpi == 1:
        try:
          email = input("Anna sähköpostiosoitteesi: ")
            
          salasana = input("Anna salasanasi: ")
        except:
          pass
  except:
    pass
except:
  pass
conn = sqlite3.connect('./Kirjasto.db')
cur = conn.cursor()

