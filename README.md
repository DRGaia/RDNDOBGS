# Kirjastojärjestelmä.

Tekijät Daniel R, Olavi L, Justus J. Tiev24P.

---

- main.py [Koodin_selkäranka]:  
- Kannat/  
   - kirjasto.db [Kanta]:
   - sqlkoodit.txt [Tekstiversio_sqlkoodista]:  
- Kirjastojärjestelmä/  
   - aika.py [Laskee_palautuspäivän_ja_kauanko_kirjaa_on_lainattu]:  
   - haku.py [Kirjan_hakeminen]:  
   - historia.py [Näyttää_asiakkaan_lainaushistorian]:  
   - kirjautuminen.py [Sisäänkirjautumisjärjestelmä]:  
   - lainaus.py [Kirjan_lainaaminen]:  
   - lisäys.py [Kirjan/henkilön_lisäys]:  
   - muokkaus.py [Käyttäjä_pystyy_muokkaamaan_omia_tietojaan]:  
   - palautus.py [Asiakkaiden_lainaukset_voidaan_palauttaa]:  
   - poisto.py [Kirjan/henkilön_poistaminen]:  
   - sakko.py [Antaa_käyttäjälle_sakot]:  
   - signin.py [Uuden_käyttäjän_luominen]:  
   - tarkistus.py [Käyttäjä_pystyy_tarkistamaan_omia_tietojaan]:  

---

# Tarkempi selitys.  
  
## main.py  
  
main.py toimii ohjelman selkärankana.  
Se ottaa kaikki muut Python-tiedostot ja asettaa ne valikoimaan, jota käyttäjä voi käyttää.  
  
## aika.py  
  
aika.py toimii varmistajana lainaajalle.  
Se laskee kauanko kirjaa on lainattu.  
Se antaa varoituksen, jos kirja on kohta myöhässä.  
Tai, jos kirja on myöhässä.  
  
## haku.py  
  
haku.py toimii ohjelman hakujärjestelmänä.  
Sillä pystyt hakemaan kirjan tai asiakaskäyttäjän.
  
## historia.py  
  
historia.py toimii adminien käyttämänä asiakastieto tarkistajana.  
Admin voi avata ja nähdä kenen tahansa muun asiakkaan tiedot ja lainaushistorian.  
  
## kirjautuminen.py  
  
kirjautuminen.py antaa käyttäjän kirjautua järjestelmään.  
Se antaa vaihtoehdon joko kirjautua adminina tai asiakkaana.  
  
## lainaus.py  
  
lainaus.py antaa adminin lainata kirjan asiakkaalle.  
Kirja menee käyttäjän lainauksiin ja pysyy sielä kunnes se on palautettu.  
Kirjaa ei voi lainata jos henkilön sakkosaldo ylittää 0 €.  
  
## lisäys.py  
  
lisäys.py antaa adminin lisätä kirjoja ja käyttäjiä.
  
## muokkaus.py  
  
muokkaus.py antaa käyttäjän muokata omia tietojaan.  
  
## palautus.py  
  
palautus.py antaa admineille oikeuden palauttaa asiakkaan lainaaman kirjan järjestelmään.  
  
## poisto.py  
  
poisto.py antaa adminin poistaa kirjan tai käyttäjän järjestelmästä.  
  
## sakko.py  
  
sakko.py antaa sakot myöhästyneistä kirjoista.  
  
## signin.py  
  
signin.py antaa muun kuin adminin luoda uuden asiakaskäyttäjän.  
  
## tarkistus.py  
  
tarkistus.py antaa käyttäjän tiedot kuten salasanan, sähköpostin, nimen, sakkosaldon ja syntymävuoden.  
  
---
