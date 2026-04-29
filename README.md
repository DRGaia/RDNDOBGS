# Kirjastojärjestelmä.

- main.py [Koodin_selkäranka]:  
- Kannat/  
   - kirjasto.db [Kanta]:  
   - kirjat.txt [Testi_kirjat]:  
   - sqlkoodit.txt [Teksti_versio_sqlkoodista]:  
- Kirjastojärjestelmä/  
   - aika.py [Laskee_palautus_päivän_ja_kauanko_kirjaa_on_lainattu]:  
   - haku.py [Kirjan_hakeminen]:  
   - historia.py [Näyttää_asiakkaan_lainaushistorian]:  
   - kirjautuminen.py [Sisäänkirjautumisjärjestelmä]:  
   - lainaus.py [Kirjan_lainaaminen]:  
   - lisäys.py [Kirjan/henkilön_lisäys]:  
   - muokkaus.py [Käyttäjä_pystyy_muokkaamaan_omia_tietoja]:  
   - palautus.py [Käyttäjän_kirjat_voidaan_palauttaa]:  
   - poisto.py [Kirjan/henkilön_poistaminen]:  
   - sakko.py [Antaa_käyttäjälle_sakot]:  
   - signin.py [Uuden_käyttäjän_luominen]:  
   - tarkistus.py [Käyttäjä_voi_tarkistaa_omia_tietoja]:  

---

# Tarkempi selitys.  
  
## main.py  
  
main.py toimii ohjelman selkärankana.  
Se ottaa kaikki muut python tiedostot ja asettaa ne valikoimaan, jota käyttäjä voi käyttää.  
  
## aika.py  
  
aika.py toimii varmistajana lainaajalle.  
Se laskee kauanko kirjaa on lainattu.  
Se antaa varoituksen jos kirja on kohta myöhässä.  
Tai jos kirja on myöhässä.  
  
## haku.py  
  
haku.py toimii ohjelman hakujärjestelmänä.  
Sillä pystyt hakemaan kirjan tai asiakas käyttäjän.
  
## historia.py  
  
historia.py toimii adminien käyttämänä asiakastieto tarkistajana.  
Admin voi avata ja nähdä minkä tahansa muun asiakkaan tiedot ja lainaushistorian.  
  
## kirjautuminen.py  
  
kirjautuminen.py antaa käyttäjän kirjautua sisälle.  
se antaa vaihtoehdon joko kirjautua adminina tai asiakkaana.  
  
## lainaus.py  
  
lainaus.py antaa adminin lainata kirjan asiakkaalle.  
Kirja menee käyttäjän lainauksiin ja pysyy sielä kunnes se on palautettu.  
Kirjaa ei voi lainata jos on sakkosaldo joka ylittää 0€.  
  
## lisäys.py  
  
lisäys.py antaa adminin lisätä kirjoja ja käyttäjiä.
  
## muokkaus.py  
  
muokkaus.py antaa käyttäjän muokata omia tietojaan.  
  
## palautus.py  
  
palautus.py antaa admineille oikeuden palauttaa asiakkaan kirjan järjestelmään.  
  
## poisto.py  
  
poisto.py antaa adminin poistaa kirjan tai käyttäjän järjestelmästä.  
  
## sakko.py  
  
sakko.py antaa sakot myöhästyneistä kirjoista.  
  
## signin.py  
  
signin.py antaa ei adminin luoda uuden asiakas käyttäjän.  
  
## tarkistus.py  
  
tarkistus.py antaa käyttäjän tiedot kuten salasanan, sähköpostin, nimen, sakkosaldon ja syntymävuoden.  
  
---
  