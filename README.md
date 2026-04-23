# Kirjastojärjestelmä.

Projektin on tarkoitus olla kirjastojärjestelmä, jossa pystys:
    Admin:
        Lisäämään kirjoja ja asiakkaita.
        Poistamaan kirjoja ja asiakkaita.
        Sakkosaldon muokkaaminen asiakkaalle.
    Asiakas:
        Etsimään kirjan.
        Lainaamaan kirjan.
        Tarkistamaan omat tiedot.
        Muokkaamaan omia tietoja.
        Tarkistaa lainattuja kirjoja.
        Saa muistutuksen palautuksesta 3 päivää ennen ja jos kirja on myöhässä.

main.py [Koodin_selkäranka]:
Kannat/
    kirjasto.db [Kanta]:
    kirjat.txt [Testi_kirjat]:
    sqlkoodit.txt [Teksti_versio_sqlkoodista]:
Kirjastojärjestelmä/
    haku.py [Kirjan_hakeminen]:
    kirjautuminen.py [Sisäänkirjautumisjärjestelmä]:
    lisäys.py [Kirjan/henkilön_lisäys]:
    poisto.py [Kirjan/henkilön_poistaminen]
    signin.py [Uuden_käyttäjän_luominen]

# Kirjoilla on nimi, kirjoittaja, julkaisuvuosi ja ISBN 
# Yhdestä kirjasta voi olla useita kappaleita  
# Kirjaa ei voi lainata, jos kaikki kappaleet ovat lainassa  
# Asiakkaalla on nimi, syntymävuosi, sähköposti ja sakkosaldo
# Asiakas voi lainata useita kirjoja
# Lainan oletusaika on 14 päivää
- Uusia lainoja ei voi tehdä, jos asiakkaalla on myöhässä olevia lainoja tai maksamattomia sakkoja
# Järjestelmänvalvojalla on nimi ja sähköposti ja kirjautuminen järjestelmään
- Järjestelmänvalvoja voi:
  # lisätä ja poistaa kirjoja
  # hakea kirjoja nimen tai kirjoittajan perusteella
  # lisätä ja poistaa asiakkaita
  # poistaa asiakkaan vain jos hänellä ei ole lainoja eikä sakkoja
  - tarkastella asiakkaan tietoja ja lainaushistoriaa
  # lisätä ja poistaa järjestelmänvalvojia
  # lainata kirjoja asiakkaille ja merkitä palautuksia
  - nollata asiakkaan sakot
- Käyttäjä voi:
  # tarkastella omia tietojaan
  - muokata nimeä ja sähköpostia
  # tarkastella lainassa olevia kirjoja
  # hakea kirjoja nimen ja kirjoittajan perusteella
- Lainoissa näytetään:
  # varoitus, jos palautukseen ≤ 3 päivää
  # erillinen merkintä, jos kirja on myöhässä
- Järjestelmässä tulee olla:
  # vähintään 10 kirjaa
  # vähintään 5 kirjailijaa
  # vähintään 3 kirjaa useilla kappaleilla
  # vähintään 5 asiakasta
  # vähintään 2 järjestelmänvalvojaa
  # osa asiakkaista joilla lainoja (myöhässäkin)
  # osa asiakkaista joilla sakkoja

- Bonukset:
  - ISBN-tarkistus lisättäessä kirjaa
  - sakot kasvavat automaattisesti 1€ / päivä / myöhässä oleva kirja
  - kirjojen varaus (7 päivää), varattu kappale ei ole lainattavissa