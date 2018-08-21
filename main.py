import tkinter as tk
import startno_okno as sto
import random as r
import sys
import os
import timeit

startno_okno = sto.Startno_okno()
startno_okno

PUF = 'puf'
ZASTAVA = 'f'
VRSTICE = sto.VRSTICE.stevilo
STOLPCI = sto.STOLPCI.stevilo
BOMBE = sto.BOMBE.stevilo
cekiranje_za_zmago = sto.Konstanta(1)
VELIKOST_GUMBA = 3

#stanja
zastava, pritisnjen, zakrit, bomba = 'zastava', 'pritisnjen', 'zakrit', 'bomba'

#okno
main_okno = tk.Tk()
main_okno.title('Minolovec')

#poravnaj okno
#sirina_okna = main_okno.winfo_reqwidth()
#dolzina_okna = main_okno.winfo_reqheight()
#sirina_ekrana = main_okno.winfo_screenwidth()
#dolzina_ekrana = main_okno.winfo_screenheight()
#pozicija_desno = int(sirina_ekrana / 2 - sirina_okna)
#pozicija_dol = int(dolzina_ekrana / 2 - dolzina_okna)
#main_okno.geometry("+{}+{}".format(pozicija_desno, pozicija_dol))

#razdeljeno okno na dva dela
zg = tk.Frame(main_okno)
sp = tk.Frame(main_okno)
zg.grid(row=1)
sp.grid(row=2)


#--------------------------------------------------------------------------------------------------------------------


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


def posuj_bombe():
    zaloga_bomb = []
    while len(zaloga_bomb) < BOMBE:
        i = r.randint(0, VRSTICE - 1)
        j = r.randint(0, STOLPCI - 1)
        tabela[i][j].je_ni_bomba = 'je'
        if tabela[i][j] not in zaloga_bomb:
            zaloga_bomb.append(tabela[i][j])
    return zaloga_bomb


def povej_gumbom_kaj_so():
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            tabela[i][j].bombasto()
            tabela[i][j].poisci_sosednje()
            tabela[i][j].poisci_stevilo_bomb()


def gumbom_prilagodi_barvo():
    tabela_barv = [None, 'dark green', 'darkOrchid4', 'navy', 'slate blue', 'gold4', 'DodgerBlue4', 'coral4', 'turquoise4']
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            if tabela[i][j] not in zaloga_bomb:
                tabela[i][j].button.config(fg=tabela_barv[int(tabela[i][j].napis)])


def preveri_zmago():
    if cekiranje_za_zmago.stevilo == 1:
        for i in range(VRSTICE):
            for j in range(STOLPCI):
                if tabela[i][j] not in zaloga_bomb:
                    if tabela[i][j].stanje != pritisnjen:
                        return False
        izpisi_koncen_napis('zmaga')


def odpri_vse():
    cekiranje_za_zmago.stevilo = 0
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            tabela[i][j].odpri_konec()


def izpisi_koncen_napis(izid):
    if izid == 'zmaga':
        napis_konec.config(text='BRAVO!', fg='VioletRed1')
        smajli.config(image=dzek)
    else:
        prvi = 'Tole pa ni šlo...'
        drugi = 'BUM! Lahko greste med Dunajske dečke.'
        tretji = 'Več sreče prihodnjič.'
        cetrti = 'SORČI! Imate še 8 življenj.'
        peti = 'Slaba... Kar hrabro na naslednje minsko polje.'
        sesti = 'Kaj pa sreča v ljubezni?'
        i = r.randint(0, 5)
        zaloga_napisov = [prvi, drugi, tretji, cetrti, peti, sesti]
        napis_konec.config(text=zaloga_napisov[i], fg='VioletRed1')
        smajli.config(image=zalosten)
    napis_konec.pack()
    #koncen_gumb.pack()
    prazna_vrstica2.pack()


def funkcija_smajli():
    if smajli.config('image')[-1] == 'pyimage2' or smajli.config('image')[-1] == 'pyimage4':
        #resetiraj isto stevilo vrstic in stolpcev?
        main_okno
        print('Ostajam prižgan.')
    else:
        main_okno.destroy()



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
        return 'Gumb ({}, {}, {})'.format(self.vrstica, self.stolpec, self.stevilka)

    def __str__(self):
        return 'Gumb na ({0}, {1}), z napisom {}'.format(self.vrstica, self.stolpec, self.stevilka)

    def prikazi(self, okno):
        return self.button.grid(row=self.vrstica, column=self.stolpec)

    def bombasto(self):
        if self.je_ni_bomba == 'je':
            self.napis = PUF

    def razkrij(self):
        self.button.config(text=self.napis)

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

    def poisci_stevilo_bomb(self):
        if self.je_ni_bomba == 'ni':
            num = 0
            for vsak in self.sosednji:
                if vsak.je_ni_bomba == 'je':
                    num += 1
            self.napis = str(num)

    def levi_klik(self):
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

    def desni_klik(self, random_stvar):
        #self.spremeni_stanje(zastava)
        if self.stanje == zakrit:
            self.spremeni_stanje(zastava)
        elif self.stanje == zastava:
            self.spremeni_stanje(zakrit)

    def odpri_sosednje(self):
        for gumb in self.sosednji:
            if gumb.stanje == zakrit:
                gumb.levi_klik()

    def lahko_odprem_sosednje(self):
        stevec = 0
        for sosed in self.sosednji:
            if sosed.stanje == zastava:
                stevec += 1
        if self.napis == str(stevec):
            return True
        return False

    def odpri_konec(self):
        if self.stanje == zakrit:
            if not(tabela[self.vrstica][self.stolpec] in zaloga_bomb):
                self.button.config(relief='sunken', bg='light grey')
                self.napis = ''
                self.spremeni_stanje(pritisnjen)
            else:
                self.button.config(text=self.napis, fg='blue', bg='light grey')

    def spremeni_stanje(self, novo_stanje):
        if novo_stanje == zastava:
            self.stanje = zastava
            self.button.config(text=ZASTAVA, fg='red')
            smajli.config(image=zacuden)
        elif novo_stanje == pritisnjen:
            self.stanje = pritisnjen
            self.button.config(text=self.napis, relief='sunken')
            if smajli.config('image')[-1] != 'pyimage3':
                smajli.config(image=vesel)
        elif novo_stanje == zakrit:
            self.stanje = zakrit
            self.button.config(text='')
            smajli.config(image=vesel)


#-----------------------------------------------------------------------------------------------------------------


#zgornji napisi za stevilo vrstic, stolpcev in bomb
zgornji_napis_cas = tk.Label(zg, text='Čas igranja:')
zgornji_napis_bombe = tk.Label(zg, text='Število bomb: {}'.format(BOMBE))
zgornji_napis_bombe.pack()
zgornji_napis_cas.pack()

#prazna vrstica
prazna_vrstica = tk.Label(zg, text='')
prazna_vrstica.pack()

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

#druga prazna vrstica
prazna_vrstica2 = tk.Label(zg, text='')
prazna_vrstica2.pack()


main_okno.mainloop()
