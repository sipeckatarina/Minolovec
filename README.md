# Minolovec 

## Projektna za UVP 
Igra je napisana v jeziku Python. Navdihnila jo je vsem znana igra Minesweeper (Minolovec). 
Namen igre je krepitev umskih sposobnosti igralca, ki mora v tabeli odpreti vsa polja, v katerih ni bombe. 

## Uvodno okno 
Ob zagonu je igralcu ponujeno okno, v katerem lahko sam doloci velikost mre�e (in s tem �tevilo polj), 
doloci �tevilo vrstic in �tevilo stolpcev. V tretje polje vpi�e �tevilo bomb, ki so nato nakljucno postavljene 
v polja. Da igralec pri dolocanju �tevila bomb ne okleva predolgo, mu aplikacija ob pritisku pa gumb "priporoci 
�tevilo bomb" ponudi prijazen celo�tevilcni del 15-odstotne vrednosti �tevila vseh polj. Ce npr. doloci 13 
vrstic in 13 stoplcev, mu za �tevilo bomb predlaga 16. 

## Igranje
Igralec lahko uporablja levi in desni gumb mi�ke. 
Levi je namenjen odpiranju polj, desni pa samo oznaci polje, za katerega igralec predvideva, da je pod 
njim bomba. 
Ko igralec odpre polje, pod katerim ni bombe, je v njem izpisano �tevilo bomb v osmih sosednjih poljih. 
Ce bombe ni v nobenem od sosednjih polj, so odprta tudi vsa ta sosednja polja. Postopek je rekurzivno 
ponovljen tudi za sosednja polja teh sosednjih polj, itd. Z odprtjem praznega polja je torej odprta 
povr�ina vseh praznih polj, ki se dr�ijo skupaj in nimajo bomb. 
Glede na �tevilo, izpisano v praznem polju, uporabnik odpira sosednja polja. 
Ko igralec glede na �tevila v poljih ugotovi kje je polje z bombo, nanj klikne z desnim gumbom in tako na polje 
postavi oznako, ki mu je v pomoc pri nadaljnjem igranju. 
Ce klikne na �e odkrito polje, okrog katerega je toliko oznak za bombo, kolikor je �tevilka, napisana v polju, 
se odkrijejo �e ostala neodkrita sosednja polja. 

## Kako koncati? 
Igra je lahko zakljucena na dva nacina: 
- Neuspe�no: levi klik na polje z bombo, ki je lahko nameren ali nenameren 
- Uspe�no: odprtje vseh polj brez bombe 

V prvem primeru je igralcu nad tabelo izpisano sporocilo v tola�bo, v drugem je z njim pohvaljen. 
Ce je igra zakljucena neuspe�no, so prikazana tudi vsa polja z bombo, polje z eksplodirano bombo je 
oznaceno posebej. 
Po uspe�no zakljuceni igri sta nad tabelo izpisana �e cas igranja in �tevilo tock, ki je izracunano po 
primernem kljucu. 
Ob kliku na gumb z obrazom (na sredini zgoraj) se odpre novo okno, v katerem so zapisana imena in dose�ki najbolj�ih 
igralcev. Ce je bila igra uspe�no zakljucena, se med rezultate vpi�e tudi trenuten dose�ek, ki pride na izpisano 
lestvico le, ce je med najbolj�imi dvanajstimi. 


## Varnost
Dandana�nji je vse vec odvisnosti od igranja spletnih iger in iger nasploh, zato ponovno igranje igre 
Minolovec deluje po principu 'vec je manj'. Za ponovno igranje je namrec potrebnih vec korakov, ki 
igralca prej odvrnejo od igre in s tem zmanj�ujejo tveganje za zasvojenost z igro Minolovec. 
Potreben je ponoven zagon in ponovno dolocanje podatkov. 
Takoj, ko opazite znake zasvojenosti z igro Minolovec, se ob kavi posvetujte z avtorjem igre, z dru�ino in/ali 
s prijatelji! 