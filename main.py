import tkinter as tk
import startno_okno as sto
import high_score_okno as hso
import random as r
from time import gmtime, strftime
import sys
import os

#startno okno
startno_okno = sto.Startno_okno()
startno_okno

#oznake, konstante
PUF = 'puf'
ZASTAVA = 'F'
IME = startno_okno.ime
VRSTICE = sto.VRSTICE.stevilo
STOLPCI = sto.STOLPCI.stevilo
BOMBE = sto.BOMBE.stevilo
cekiranje_za_zmago = sto.Konstanta(1)
zacni_steti_cas=sto.Konstanta(1)
VELIKOST_GUMBA = 3
CAS = sto.Konstanta(0)
TOCKE = sto.Konstanta(0)

#stanja
zastava, pritisnjen, zakrit, bomba = 'zastava', 'pritisnjen', 'zakrit', 'bomba'

#okno
main_okno = tk.Tk()
main_okno.title('Minolovec')

#razdeljeno okno na dva dela
zg = tk.Frame(main_okno)
sp = tk.Frame(main_okno)
zg.grid(row=1)
sp.grid(row=2)

#nastavek za cas
cas_zacetek = sto.Konstanta(0)
cas_konec = sto.Konstanta(0)


#--------------------------------------------------------------------------------------------------------------------


#naredi tabelo
def naredi_tabelo():
    tab = []
    for i in range(VRSTICE):
        v = []
        for j in range(STOLPCI):
            g = Gumb(i, j)
            v.append(g)
            g.prikazi(sp)
        tab.append(v)
    return tab


#doloci bombe
def posuj_bombe():
    zaloga_bomb = []
    while len(zaloga_bomb) < BOMBE:
        i = r.randint(0, VRSTICE - 1)
        j = r.randint(0, STOLPCI - 1)
        tabela[i][j].je_ni_bomba = 'je'
        if tabela[i][j] not in zaloga_bomb:
            zaloga_bomb.append(tabela[i][j])
    return zaloga_bomb


#cifra ali puf
def povej_gumbom_kaj_so():
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            tabela[i][j].bombasto()
            tabela[i][j].poisci_sosednje()
            tabela[i][j].poisci_stevilo_bomb()


#barva
def gumbom_prilagodi_barvo():
    tabela_barv = [None, 'dark green', 'darkOrchid4', 'navy', 'slate blue', 'gold4', 'DodgerBlue4', 'coral4', 'turquoise4']
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            if tabela[i][j] not in zaloga_bomb:
                tabela[i][j].button.config(fg=tabela_barv[int(tabela[i][j].napis)])


#zmaga?
def preveri_zmago():
    if cekiranje_za_zmago.stevilo == 1:
        for i in range(VRSTICE):
            for j in range(STOLPCI):
                if tabela[i][j] not in zaloga_bomb:
                    if tabela[i][j].stanje != pritisnjen:
                        return False
        izracunaj_cas('koncni')
        izracunaj_stevilo_tock()
        izpisi_koncen_napis('zmaga')


#konecno odpiranje
def odpri_vse():
    cekiranje_za_zmago.stevilo = 0
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            tabela[i][j].odpri_konec()


#napisi
def izpisi_koncen_napis(izid):
    if izid == 'zmaga':
        napis_konec.config(text='BRAVO, {}!'.format(IME), fg='VioletRed1')
        smajli.config(image=dzek)
        izpisi_cas()
        izpisi_stevilo_tock()
    else:
        prvi = 'Tole pa ni šlo...'
        drugi = 'BUM! Lahko greste med Dunajske dečke.'
        tretji = 'Opala ... Več sreče prihodnjič.'
        cetrti = 'SORČI! Imate še 8 življenj.'
        peti = 'Slaba ... Kar hrabro na naslednje minsko polje.'
        sesti = 'Saj bo več sreče v ljubezni.'
        sedmi = 'Bo pa treba še nekaj žgancev!'
        i = r.randint(0, 6)
        zaloga_napisov = [prvi, drugi, tretji, cetrti, peti, sesti, sedmi]
        napis_konec.config(text=zaloga_napisov[i], fg='VioletRed1')
        smajli.config(image=zalosten)
    napis_konec.pack()
    prazna_vrstica.pack()


#smajli
def funkcija_smajli():
    if smajli.config('image')[-1] == 'pyimage2' or smajli.config('image')[-1] == 'pyimage4':
        #resetiraj isto stevilo vrstic in stolpcev?
        main_okno
        print('Kar ste začeli, to končajte.')
    if smajli.config('image')[-1] == 'pyimage1':
        hso.High_score_okno(IME, izracunaj_stevilo_tock(), 'ja')
        main_okno.destroy()
    else:
        hso.High_score_okno(IME, izracunaj_stevilo_tock(), 'ne')
        main_okno.destroy()


#cas - racznanje
def izracunaj_cas(zacetni_ali_koncni):
    cas = strftime("%H %M %S", gmtime())
    razdri = cas.split(' ')
    if zacetni_ali_koncni == 'zacetni':
        cas_zacetek.stevilo = int(razdri[0]) * 3600 + int(razdri[1]) * 60 + int(razdri[2])
    else:
        cas_konec.stevilo = int(razdri[0]) * 3600 + int(razdri[1]) * 60 + int(razdri[2])


#vrne seznam [minute, sekunde]
def cas_igranja(zacetni, koncni):
    cas = koncni - zacetni
    minute = cas // 60
    sekunde = cas % 60
    if minute == 0 and sekunde == 0:
        sekunde = 1
        cas = 1
    CAS.stevilo = cas
    return [minute, sekunde]


#cas - pisanje
def izpisi_cas():
    minute, sekunde = cas_igranja(cas_zacetek.stevilo, cas_konec.stevilo)
    if minute == 0:
        napis_cas.config(text='Igrali ste {} sekund.'.format(sekunde))
    elif minute == 1:
        napis_cas.config(text='Igrali ste 1 minuto in {} sekund.'.format(sekunde))
    elif minute == 2:
        napis_cas.config(text='Igrali ste {} minuti in {} sekund.'.format(minute, sekunde))
    elif minute in [3, 4]:
        napis_cas.config(text='Igrali ste {} minute in {} sekund.'.format(minute, sekunde))
    else:
        napis_cas.config(text='Igrali ste {} minut in {} sekund.'.format(minute, sekunde))
    napis_cas.pack()


#tocke
def izracunaj_stevilo_tock():
    cas = cas_igranja(cas_zacetek.stevilo, cas_konec.stevilo)
    if BOMBE < VRSTICE * STOLPCI - 3:
        cas = cas[0] * 60 + cas[1]
        delez_bomb = BOMBE / (VRSTICE * STOLPCI)
        rezultat = VRSTICE * STOLPCI * (delez_bomb ** 2) / cas
        if VRSTICE * STOLPCI < 100:
            TOCKE.stevilo = int(rezultat * 8000)
            return int(rezultat * 8000)
        else:
            TOCKE.stevilo = int(rezultat * 10000)
            return int(rezultat * 10000)
    else: return 0


#izpisi tocke
def izpisi_stevilo_tock():
    napis_stevilo_tock.config(text='Dosegli ste {} točk.'.format(TOCKE.stevilo))
    napis_stevilo_tock.pack()


#gumbi
class Gumb():

    def __init__(self, vrstica, stolpec, napis=None, okno=sp, stanje='zakrit', je_ni_bomba='ni'):
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.napis = napis
        self.stanje = stanje
        self.je_ni_bomba = je_ni_bomba
        self.button = tk.Button(okno, text='', width=VELIKOST_GUMBA, height=VELIKOST_GUMBA//2, command=self.levi_klik, relief='raised')
        self.button.bind('<Button-3>', self.desni_klik)

    def __repr__(self):
        return 'Gumb ({}, {}, {})'.format(self.vrstica, self.stolpec, self.napis)

    def __str__(self):
        return 'Gumb na ({0}, {1}), z napisom {}'.format(self.vrstica, self.stolpec, self.napis)

    #klice jo naredi_tabelo (zunanja)
    def prikazi(self, okno):
        return self.button.grid(row=self.vrstica, column=self.stolpec)

    #klice jo povej_gumbom_kaj_so (zunanja)
    def bombasto(self):
        if self.je_ni_bomba == 'je':
            self.napis = PUF

    #klice jo povej_gumbom_kaj_so (zunanja)
    def poisci_sosednje(self):
        self.sosednji = []
        #vrstica zgoraj
        if not(self.vrstica == 0):
            self.gumb_gor = tabela[self.vrstica - 1][self.stolpec]
            self.sosednji.append(self.gumb_gor)
            if not(self.stolpec == 0):
                self.gumb_levo_gor = tabela[self.vrstica - 1][self.stolpec - 1]
                self.sosednji.append(self.gumb_levo_gor)
            if not(self.stolpec == STOLPCI - 1):
                self.gumb_desno_gor = tabela[self.vrstica - 1][self.stolpec + 1]
                self.sosednji.append(self.gumb_desno_gor)
        #vrstica spodaj
        if not(self.vrstica == VRSTICE - 1):
            self.gumb_dol = tabela[self.vrstica + 1][self.stolpec]
            self.sosednji.append(self.gumb_dol)
            if not(self.stolpec == 0):
                self.gumb_levo_dol = tabela[self.vrstica + 1][self.stolpec - 1]
                self.sosednji.append(self.gumb_levo_dol)
            if not(self.stolpec == STOLPCI - 1):
                self.gumb_desno_dol = tabela[self.vrstica + 1][self.stolpec + 1]
                self.sosednji.append(self.gumb_desno_dol)
        #levi in desni sosed
        if not(self.stolpec == 0):
            self.gumb_levo = tabela[self.vrstica][self.stolpec - 1]
            self.sosednji.append(self.gumb_levo)
        if not(self.stolpec == STOLPCI - 1):
            self.gumb_desno = tabela[self.vrstica][self.stolpec + 1]
            self.sosednji.append(self.gumb_desno)

    #klice jo povej_gumbom_kaj_so (zunanja)
    def poisci_stevilo_bomb(self):
        if self.je_ni_bomba == 'ni':
            num = 0
            for vsak in self.sosednji:
                if vsak.je_ni_bomba == 'je':
                    num += 1
            self.napis = str(num)

    #klice jo levi klik, odpir_sosednje
    def levi_klik(self):
        if zacni_steti_cas.stevilo == 1:
            izracunaj_cas('zacetni')
            zacni_steti_cas.stevilo = 0
        if self.stanje == zakrit:
            if self.je_ni_bomba == 'je':
                smajli.config(image=zalosten)
                izpisi_koncen_napis('ni slo')
                odpri_vse()
                self.button.config(fg='red')
            else:
                self.spremeni_stanje(pritisnjen)
                if self.napis == '0':
                    self.odpri_sosednje()
                    self.napis = ''
            self.spremeni_stanje(pritisnjen)
        else:
            if self.lahko_odprem_sosednje() == True:
                self.odpri_sosednje()
        preveri_zmago()

    #klice jo desni klik
    def desni_klik(self, random_stvar):
        #self.spremeni_stanje(zastava)
        if self.stanje == zakrit:
            self.spremeni_stanje(zastava)
        elif self.stanje == zastava:
            self.spremeni_stanje(zakrit)

    #klice jo levi_klik
    def odpri_sosednje(self):
        for gumb in self.sosednji:
            if gumb.stanje == zakrit:
                gumb.levi_klik()

    #klice jo levi_klik
    def lahko_odprem_sosednje(self):
        stevec = 0
        for sosed in self.sosednji:
            if sosed.stanje == zastava:
                stevec += 1
        if self.napis == str(stevec):
            return True
        return False

    #klice jo odpri_vse (zunanja)
    def odpri_konec(self):
        if self.stanje == zakrit:
            if not(tabela[self.vrstica][self.stolpec] in zaloga_bomb):
                self.napis = ''
                self.spremeni_stanje(pritisnjen)
                self.button.config(relief='sunken', bg='grey80')
            else:
                self.button.config(text=self.napis, fg='blue', bg='grey83')
                self.button.config(command=self.onesposobi)

    #klice jo odpri_konec
    def onesposobi(self):
        return True

    #klice jo odpri_kones, desni_klik, levi_klik
    def spremeni_stanje(self, novo_stanje):
        if novo_stanje == zastava:
            self.stanje = zastava
            self.button.config(text=ZASTAVA, fg='red')
            smajli.config(image=zacuden)
        elif novo_stanje == pritisnjen:
            self.stanje = pritisnjen
            self.button.config(text=self.napis, relief='sunken', bg='grey91')
            if smajli.config('image')[-1] != 'pyimage3':
                smajli.config(image=vesel)
        elif novo_stanje == zakrit:
            self.stanje = zakrit
            self.button.config(text='')
            smajli.config(image=vesel)


#-----------------------------------------------------------------------------------------------------------------


#zgornji napisi za stevilo vrstic, stolpcev in bomb
zgornji_napis_bombe = tk.Label(zg, text='Število bomb: {}'.format(BOMBE))
zgornji_napis_bombe.pack()

#prazna vrstica
prazna_vrstica = tk.Label(zg, text='')
#prazna_vrstica.pack()

#napis in gumb za konec igre
napis_konec = tk.Label(zg, text='', fg='red')
#koncen_gumb = tk.Button(zg, text='Zapri', command=zapri)

#mreža z gumbi
tabela = naredi_tabelo()
zaloga_bomb = posuj_bombe()
povej_gumbom_kaj_so()
gumbom_prilagodi_barvo()

#smajli
dzek = tk.PhotoImage(file='dzek.png')
vesel = tk.PhotoImage(file='vesel.png')
zalosten = tk.PhotoImage(file='zalosten.png')
zacuden = tk.PhotoImage(file='zacuden.png')

#postavi smajlija
smajli=tk.Button(zg, image=vesel, command=funkcija_smajli)
#smajli.config(width=26, height=26)
smajli.pack()

#cas, tocke
napis_cas = tk.Label(zg, text='')
napis_stevilo_tock = tk.Label(zg, text='')

main_okno.mainloop()