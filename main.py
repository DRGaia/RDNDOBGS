from Kirjastojärjestelmä import kirjautuminen, lisäys, poisto, haku, lainaus, palautus, aika;
while True:
    kirjautuminen.logsignin()
    admin = kirjautuminen.admin
    asiakas = kirjautuminen.asiakas
    if admin == True:
        while True:
                print("Mitä haluat tehdä (a = vain admineille)? \n\n a1) Kirjan lisäys \n\n a2) Kirjan lainaus \n\n a3) Kirjan palautus \n\n a4) Kirjan, asiakkaan tai adminin poistaminen \n\n a5) Myöhästysten tarkastelu \n\n 1) Kirjan hakeminen \n")
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
                else:
                    print("\n Kirjoita mitä haluat tehdä (a1, a2, a3, a4, a5 tai 1) \n")
    elif asiakas == True:
        print("Mitä haluat tehdä? \n\n 1) Kirjan hakeminen \n")
        mikä = input()
        if mikä == "1":
            haku.haku()
        else:
            print("\n Kirjoita mitä haluat tehdä (1, 2 tai 3)")