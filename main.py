from Kirjastojärjestelmä import kirjautuminen, lisäys, poisto, haku, tarkistus, lainaus, palautus, aika, sakko, muokkaus, historia;

while True:
    kirjautuminen.logsignin()
    admin = kirjautuminen.admin
    asiakas = kirjautuminen.asiakas
    käyt = kirjautuminen.käyt
    if admin == True:
        while True:
            print("Mitä haluat tehdä (a = vain admineille)? \n\n a1) Kirjan lisäys \n\n a2) Kirjan lainaus \n\n a3) Kirjan palautus \n\n a4) Kirjan, asiakkaan tai adminin poistaminen \n\n a5) Myöhästysten tarkastelu \n\n a6) Sakkojen päivittäminen \n\n a7) Sakko saldon nollaus \n\n a8) Asiakkaan tietojen ja lainausten tarkastelu \n\n 1) Kirjan hakeminen  \n\n 2) Omien tietojen tarkastelu \n")
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
            elif mikä == "a7":
                sakko.sakonpoisto()
            elif mikä == "a8":
                historia.historia()
            elif mikä == "1":
                haku.haku()
            elif mikä == "2":
                tarkistus.tarkistus(admin,asiakas,käyt)
            elif mikä == "3":
                muokkaus.muokkaus(admin,asiakas,käyt)
            else: 
                print("\n Kirjoita mitä haluat tehdä (a1, a2, a3, a4, a5, a6, a7, a8, 1, 2 tai 3)")
    elif asiakas == True:
        while True:
            print("\n 1) Kirjan hakeminen \n\n 2) Käyttäjätiedot \n\n 3) Omien tietojen muokkaus \n")
            mikä = input()
            if mikä == "1":
                    haku.haku()
            elif mikä == "2":
                tarkistus.tarkistus(admin,asiakas,käyt)
            elif mikä == "3":
                muokkaus.muokkaus(admin,asiakas,käyt)
            else: 
                print("\n Kirjoita mitä haluat tehdä (1, 2 tai 3)")
