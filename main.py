# tukaj je leđit koda ... v nastajanju
import tkinter as tk
import startno_okno as sto
import random as r
#import gumbi as g
#from gumbi import Gumb

PUF = 'puf'
ZASTAVA = 'f'
VRSTICE = sto.VRSTICE.stevilo
STOLPCI = sto.STOLPCI.stevilo
BOMBE = sto.BOMBE.stevilo

velikost_gumba = sto.Konstanta(50//int(max(VRSTICE, STOLPCI)))
VELIKOST_GUMBA = velikost_gumba.stevilo

zastava, pritisnjen, zakrit, bomba = 'zastava', 'pritisnjen', 'zakrit', 'bomba'

main_okno = tk.Tk()
main_okno.title('Minolovec (upam)')
#main_okno.geometry("500x500") #velikost okna

#razdeljeno okno na dva dela
zg = tk.Frame(main_okno)
sp = tk.Frame(main_okno)
zg.grid(row=1)
sp.grid(row=2)


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


def odpri_vse():
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            tabela[i][j].odpri_konec()


def izpisi_koncen_napis(izid):
    if izid == 'zmaga':
        napis_konec.config(text='BRAVO!')
    else:
        prvi = 'Tole pa ni šlo...'
        drugi = 'BUM, lahko greste med Dunajske dečke.'
        tretji = 'Več sreče prihodnjič.'
        cetrti = 'SORČI! Imate še 8 življenj.'
        peti = 'Slaba... Kar hrabro na naslednje minsko polje.'
        i = r.randint(0, 4)
        zaloga_napisov = [prvi, drugi, tretji, cetrti, peti]
        napis_konec.config(text=zaloga_napisov[i], fg='red')
        napis_konec.pack()
        koncen_gumb.pack()
        prazna_vrstica2.pack()


def zapri():
    main_okno.destroy()


class Gumb():

    def __init__(self, vrstica, stolpec, stevilka=None, okno=sp, stanje='zakrit'):
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.stevilka = stevilka
        self.napis = str(stevilka)
        self.stanje = stanje
        self.button = tk.Button(okno, text='', width=VELIKOST_GUMBA, height=VELIKOST_GUMBA//2, command=self.levi_klik, relief='raised')
        self.button.bind('<Button-3>', self.desni_klik)

    def __repr__(self):
        return 'Gumb ({}, {}, {})'.format(self.vrstica, self.stolpec, self.stevilka)

    def __str__(self):
        return 'Gumb na ({0}, {1}), z napisom {}'.format(self.vrstica, self.stolpec, self.stevilka)

    def prikazi(self, okno):
        return self.button.grid(row=self.vrstica, column=self.stolpec)

    def razkrij(self):
        self.button.config(text=self.napis)

    def levi_klik(self):
        if self.button.config('relief')[-1] != 'sunken':
            self.button.config(relief='sunken')
            if self.napis == PUF:
                self.button.config(fg='red')
                izpisi_koncen_napis('ni slo')
                odpri_vse()
            else:
                self.poisci_sosednje()
                self.poisci_stevilo_bomb()
                if self.napis == '0':
                    self.odpri_sosednje()
                    self.napis = ''
            self.button.config(text=self.napis)

    def desni_klik(self, random_stvar):
        self.stanje = zastava
        if self.button.config('relief')[-1] == 'raised':
            self.button.config(text=ZASTAVA, fg='red')


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

    def odpri_sosednje(self):
        for gumb in self.sosednji:
            gumb.levi_klik()

    def poisci_stevilo_bomb(self):
        self.poisci_sosednje()
        num = 0
        for vsak in self.sosednji:
            if vsak.napis == PUF:
                num += 1
        self.napis = str(num)

    def odpri_konec(self):
        if self.button.config('relief')[-1] != 'sunken':
            if self.button.config('text')[-1] != ZASTAVA:
                if not(tabela[self.vrstica][self.stolpec] in zaloga_bomb):
                    self.button.config(relief='sunken', bg='light grey')
                else:
                    self.button.config(text=self.napis, fg='blue', bg='light grey')

    def spremeni_stanje(self, novo_stanje):
        if novo_stanje == zastava:
            self.stanje = zastava
            self.button.config(text=ZASTAVA, fg='red')
        elif novo_stanje == pritisnjen:
            self.stanje = pritisnjen
            self.button.config(text=self.napis, relief='sunken')
        elif novo_stanje == zakrit:
            self.stanje = zakrit
            self.button.config(text='')
        else:
            self.stanje = bomba


############################################################################################################################


#mreža z gumbi
tabela = naredi_tabelo()

#zgornji napisi za stevilo vrstic, stolpcev in bomb
zgornji_napis_vrstice = tk.Label(zg, text='Število vrstic: {}'.format(VRSTICE))
zgornji_napis_stolpci = tk.Label(zg, text='Število stolpcev: {}'.format(STOLPCI))
zgornji_napis_bombe = tk.Label(zg, text='Število bomb: {}'.format(BOMBE)) #tukaj je treba se popraviti stvari
zgornji_napis_vrstice.pack()
zgornji_napis_stolpci.pack()
zgornji_napis_bombe.pack()

#prazna vrstica
prazna_vrstica = tk.Label(zg, text='')
prazna_vrstica.pack()
prazna_vrstica2 = tk.Label(zg, text='')

#napis in gumb za konec igre
napis_konec = tk.Label(zg, text='', fg='red')
koncen_gumb = tk.Button(zg, text='Nova igra', command=zapri)

#na random izbrane bombe, seznam bomb (zaloga_bomb)
zaloga_bomb = []
while len(zaloga_bomb) < BOMBE:
    i = r.randint(0, VRSTICE - 1)
    j = r.randint(0, STOLPCI - 1)
    tabela[i][j].napis = PUF
    tabela[i][j].button.config(fg='red')
    tabela[i][j].stanje = 'bomba'
    if tabela[i][j] not in zaloga_bomb:
        zaloga_bomb.append(tabela[i][j])

main_okno.mainloop()
