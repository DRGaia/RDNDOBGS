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

conn = sqlite3.connect('./Kirjasto.db')
cur = conn.cursor()

