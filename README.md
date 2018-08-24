# Minolovec 

## Projektna za UVP 
Igra je napisana v jeziku Python. Navdihnila jo je vsem znana igra Minesweeper (Minolovec). 
Namen igre je krepitev umskih sposobnosti igralca, ki mora v tabeli odpreti vsa polja, v katerih ni bombe. 

## Uvodno okno 
Ob zagonu je igralcu ponujeno okno, v katerem lahko sam doloci velikost mreže (in s tem število polj), 
doloci število vrstic in število stolpcev. V tretje polje vpiše število bomb, ki so nato nakljucno postavljene 
v polja. Da igralec pri dolocanju števila bomb ne okleva predolgo, mu aplikacija ob pritisku pa gumb "priporoci 
število bomb" ponudi prijazen celoštevilcni del 15-odstotne vrednosti števila vseh polj. Ce npr. doloci 13 
vrstic in 13 stoplcev, mu za število bomb predlaga 16. 

## Igranje
Igralec lahko uporablja levi in desni gumb miške. 
Levi je namenjen odpiranju polj, desni pa samo oznaci polje, za katerega igralec predvideva, da je pod 
njim bomba. 
Ko igralec odpre polje, pod katerim ni bombe, je v njem izpisano število bomb v osmih sosednjih poljih. 
Ce bombe ni v nobenem od sosednjih polj, so odprta tudi vsa ta sosednja polja. Postopek je rekurzivno 
ponovljen tudi za sosednja polja teh sosednjih polj, itd. Z odprtjem praznega polja je torej odprta 
površina vseh praznih polj, ki se držijo skupaj in nimajo bomb. 
Glede na število, izpisano v praznem polju, uporabnik odpira sosednja polja. 
Ko igralec glede na števila v poljih ugotovi kje je polje z bombo, nanj klikne z desnim gumbom in tako na polje 
postavi oznako, ki mu je v pomoc pri nadaljnjem igranju. 
Ce klikne na že odkrito polje, okrog katerega je toliko oznak za bombo, kolikor je številka, napisana v polju, 
se odkrijejo še ostala neodkrita sosednja polja. 

## Kako koncati? 
Igra je lahko zakljucena na dva nacina: 
- Neuspešno: levi klik na polje z bombo, ki je lahko nameren ali nenameren 
- Uspešno: odprtje vseh polj brez bombe 

V prvem primeru je igralcu nad tabelo izpisano sporocilo v tolažbo, v drugem je z njim pohvaljen. 
Ce je igra zakljucena neuspešno, so prikazana tudi vsa polja z bombo, polje z eksplodirano bombo je 
oznaceno posebej. 
Po uspešno zakljuceni igri sta nad tabelo izpisana še cas igranja in število tock, ki je izracunano po 
primernem kljucu. 
Ob kliku na gumb z obrazom (na sredini zgoraj) se odpre novo okno, v katerem so zapisana imena in dosežki najboljših 
igralcev. Ce je bila igra uspešno zakljucena, se med rezultate vpiše tudi trenuten dosežek, ki pride na izpisano 
lestvico le, ce je med najboljšimi dvanajstimi. 


## Varnost
Dandanašnji je vse vec odvisnosti od igranja spletnih iger in iger nasploh, zato ponovno igranje igre 
Minolovec deluje po principu 'vec je manj'. Za ponovno igranje je namrec potrebnih vec korakov, ki 
igralca prej odvrnejo od igre in s tem zmanjšujejo tveganje za zasvojenost z igro Minolovec. 
Potreben je ponoven zagon in ponovno dolocanje podatkov. 
Takoj, ko opazite znake zasvojenosti z igro Minolovec, se ob kavi posvetujte z avtorjem igre, z družino in/ali 
s prijatelji! 