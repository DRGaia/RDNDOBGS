import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('./Kannat/Kirjasto.db')
cur = conn.cursor()
def lisäys():

    print("")
    valinta = input("Haluatko lisätä (k)irjan vai (a)siakkaan: ").lower()
    print("")

    if valinta == "k":
                
                while True:
                    liskirnimi = input('Anna lisättävän kirjan nimi: ')

                    print("")

                    liskirkirj = input(f'Anna kirjan "{liskirnimi}" kirjoittaja: ')

                    print("")

                    # Tarkistetaan, että syöte on kokonaisluku
                    while True:
                        liskirvuos = (input(f'Anna kirjan "{liskirnimi}" julkaisuvuosi: '))
                        try:
                            liskirvuos = int(liskirvuos)
                            print("")
                            break
                        except:
                            print("Pitää olla kokonaisluku.")

                    # Tarkistetaan, että syöte on kokonaisluku ja 13 numeroa pitkä     
                    while True:
                        liskirisbn = input(f'Anna kirjan "{liskirnimi}" ISBN-13: ')
                        if len(liskirisbn) == 13 and liskirisbn.isdigit():
                            liskirisbn = int(liskirisbn)
                            print("")
                            break
                        else:
                            print("Pitää olla 13 numeroa pitkä")

                    while True:
                        liskirkirjmäärä = input(f'Kuinka monta kappaletta kirjaa "{liskirnimi}" lisätään: ')

                        # Tarkistetaan, että syöte on kokonaisluku
                        if liskirkirjmäärä.isdigit():
                            liskirkirjmäärä = int(liskirkirjmäärä)
                            
                            # Tarkistetaan, että syöte on yli 0
                            if liskirkirjmäärä > 0:
                                print("")
                                break
                            else:
                                print("Täytyy olla suurempi kuin 0.")
                        else:
                            print("Pitää olla kokonaisluku.")
                    
                    cur.execute('INSERT INTO kirjat (nimi, kirjoittaja, julkaisuvuosi, kappalemäärä, ISBN) VALUES (?, ?, ?, ?, ?)', (liskirnimi, liskirkirj, liskirvuos, liskirkirjmäärä, liskirisbn))
                    cur.execute('SELECT * FROM kirjat')
                    data = cur.fetchall()
                    table = tabulate(data)
                    conn.commit()
                    print(table)
                    print("")
                    break

    if valinta == "a":

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

    if valinta != "a" and valinta != "k":
                print("Kirjoita k tai a! ")