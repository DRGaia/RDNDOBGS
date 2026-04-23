from Kirjastojärjestelmä import kirjautuminen, lisäys, poisto, haku, tarkistus, lainaus, palautus, aika, sakko;

while True:
    kirjautuminen.logsignin()
    admin = kirjautuminen.admin
    asiakas = kirjautuminen.asiakas
    käyt = kirjautuminen.käyt
    if admin == True:
        while True:
            print("Mitä haluat tehdä (a = vain admineille)? \n\n a1) Kirjan lisäys \n\n a2) Kirjan lainaus \n\n a3) Kirjan palautus \n\n a4) Kirjan, asiakkaan tai adminin poistaminen \n\n a5) Myöhästysten tarkastelu \n\n a6) Sakkojen päivittäminen \n\n 1) Kirjan hakeminen  \n\n 2) Omien tietojen tarkastelu \n")
            mikä = input()
            if mikä == "a1":
                lisäys.lisäys()
            elif mikä == "a2":
                lainaus.lainaus()
            elif mikä == "a3":
                palautus.palautus()
            elif mikä == "a4":
                poisto.poisto()
            elif mikä == "a5":
                aika.aika()
            elif mikä == "a6":
                sakko.sakko()
            elif mikä == "1":
                haku.haku()
            elif mikä == "2":
                tarkistus.tarkistus(admin,asiakas,käyt)
    elif asiakas == True:
        while True:
            print("\n1) Kirjan hakeminen\n\n2) Käyttäjätiedot\n")
            mikä = input()
            if mikä == "1":
                    haku.haku()
            elif mikä == "2":
                tarkistus.tarkistus(admin,asiakas,käyt)
            else: 
                print("\n Kirjoita mitä haluat tehdä (1, 2 tai 3)")
