from Kirjastojärjestelmä import kirjautuminen, lisäys, poisto, haku, lainaus;
while True:
    kirjautuminen.logsignin()
    admin = kirjautuminen.admin
    asiakas = kirjautuminen.asiakas
    if admin == True:
        while True:
            print("\n Mitä haluat tehdä? \n Admin: \n a1) Kirjan lisäys \n\n a2) Lainata kirjan \n\n a3) Kirjan poistaminen \n\n 1) Kirjan hakeminen \n")
            mikä = input()
            if mikä == "a1":
                lisäys.lisäys()
            elif mikä == "a2":
                lainaus.lainaus()
            elif mikä == "a3":
                poisto.poisto()
            elif mikä == "1":
                haku.haku()
    elif asiakas == True:
        print("\n1) Kirjan hakeminen\n")
        mikä = input()
        if mikä == "1":
                haku.haku()