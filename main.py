from Kirjastojärjestelmä import kirjautuminen, lisäys, poisto, haku, tarkistus, lainaus, palautus, aika;
while True:
    kirjautuminen.logsignin()
    admin = kirjautuminen.admin
    asiakas = kirjautuminen.asiakas
    käyt = kirjautuminen.käyt
    if admin == True:
        while True:
            print("\nMitä haluat tehdä? \nAdmin: \na1) Kirjan lisäys\n\na2) Kirjan poistaminen\n\n1) Kirjan hakeminen\n2) Käyttäjätiedot\n")
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