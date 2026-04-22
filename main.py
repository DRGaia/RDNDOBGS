from Kirjastojärjestelmä import kirjautuminen, lisäys, poisto, haku, tarkistus;
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
                poisto.poisto()
            elif mikä == "1":
                haku.haku()
            elif mikä == "2":
                tarkistus.tarkistus(admin,asiakas,käyt)
    elif asiakas == True:
        while True:
            print("\n1) Kirjan hakeminen\n2) Käyttäjätiedot\n")
            mikä = input()
            if mikä == "1":
                    haku.haku()
            elif mikä == "2":
                tarkistus.tarkistus(admin,asiakas,käyt)