# tukaj je leđit koda ... v nastajanju
import tkinter as tk
import startno_okno as sto
import random as r
#import gumbi as g
#from gumbi import Gumb

PUF = 'puf'
VRSTICE = sto.VRSTICE.stevilo
STOLPCI = sto.STOLPCI.stevilo
BOMBE = sto.BOMBE.stevilo

velikost_gumba = sto.Konstanta(50//int(max(VRSTICE, STOLPCI)))
VELIKOST_GUMBA = velikost_gumba.stevilo

main_okno = tk.Tk()
main_okno.title('Minolovec (upam)')
#main_okno.geometry("500x500") #velikost okna

#razdeljeno okno na dva dela
zg = tk.Frame(main_okno)
sp = tk.Frame(main_okno)
zg.grid(row=1)
sp.grid(row=2)

#def naredi_zastavico():

def odpri_vse():
    for i in range(VRSTICE):
        for j in range(STOLPCI):
            tabela[i][j].odpri_konec()

class Gumb():

    def __init__(self, vrstica, stolpec, stevilka=None, stanje=0, okno=sp):
        #stanje 0 = nepritisnjen, stanje 1 je pritisnjen
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.stanje = stanje
        self.stevilka = stevilka
        self.velikost = VELIKOST_GUMBA
        self.napis = str(stevilka)
        self.button = tk.Button(okno, text='', width=self.velikost, height=self.velikost//2, command=self.levi_klik, relief='raised')

    def __repr__(self):
        return 'Gumb ({}, {}, {}, {})'.format(self.vrstica, self.stolpec, self.stanje, self.stevilka)

    def __str__(self):
        stan = 5
        if self.stanje == 0:
            stan = 'nepritisnjen'
        else: stan = 'pritisnjen'
        return 'Gumb na ({0}, {1}), '.format(self.vrstica, self.stolpec) + stan + ' s stevilko {}.'.format(self.stevilka)

    def prikazi(self, okno):
        return self.button.grid(row=self.vrstica, column=self.stolpec)

    def razkrij(self):
        self.button.config(text=self.napis)

    def levi_klik(self):
        if self.button.config('relief')[-1] != 'sunken':
            self.button.config(relief='sunken')
            if self.napis == PUF:
                napis_konec.pack()
                odpri_vse()
            else:
                self.poisci_sosednje()
                self.poisci_stevilo_bomb()
                if self.napis == 0:
                    self.odpri_sosednje()
                    self.napis = ''
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

    def odpri_sosednje(self):
#        self.poisci_sosednje()
        for gumb in self.sosednji:
            gumb.levi_klik()

    def poisci_stevilo_bomb(self):
        self.poisci_sosednje()
        num = 0
        for vsak in self.sosednji:
            if vsak.napis == PUF:
                num += 1
        self.napis = num

    def odpri_konec(self):
        if self.button.config('relief')[-1] != 'sunken':
            if not(tabela[self.vrstica][self.stolpec] in zaloga_bomb):
                self.button.config(relief='sunken', text='-', fg='blue')
            else:
                self.button.config(text=self.napis, fg='blue')


############################################################################################################################


#mreža z gumbi
tabela = []
for i in range(VRSTICE):
    v = []
    for j in range(STOLPCI):
        g = Gumb(i, j)
        v.append(g)
        g.prikazi(sp)
    tabela.append(v)


#zgornji napisi za stevilo vrstic, stolpcev in bomb
zgornji_napis_vrstice = tk.Label(zg, text='Število vrstic: {}'.format(VRSTICE))
zgornji_napis_stolpci = tk.Label(zg, text='Število stolpcev: {}'.format(STOLPCI))
zgornji_napis_bombe = tk.Label(zg, text='Število neoznačenih bomb: {}'.format(BOMBE)) #tukaj je treba se popraviti stvari
zgornji_napis_vrstice.pack()
zgornji_napis_stolpci.pack()
zgornji_napis_bombe.pack()

#prazna vrstica
prazna_vrstica = tk.Label(zg, text='')
prazna_vrstica.pack()
prazna_vrstica2 = tk.Label(sp, text='')
prazna_vrstica2.grid(row=VRSTICE+1, column=STOLPCI//2)

#spodnji gumb 'BOMBA'
gumb_za_zastavico = tk.Button(sp, text='BOMBA', height=VELIKOST_GUMBA//2, width=VELIKOST_GUMBA)#, command=naredi_zastavico)
gumb_za_zastavico.grid(row=VRSTICE+2, column=STOLPCI//2)

#osnova za seznam gumbov z bombani
zaloga_bomb = []

#napis za konec igre
napis_konec = tk.Label(zg, text='SORČI! ... Kar hrabro na drugo minsko poje. ;)', fg='red')

#na random izbrane bombe
for krneki in range(BOMBE):
    i = r.randint(0, VRSTICE - 1)
    j = r.randint(0, STOLPCI - 1)
    tabela[i][j].napis = PUF
    tabela[i][j].button.config(fg='red')
    zaloga_bomb.append(tabela[i][j])

main_okno.mainloop()

#krajni, odpiranje sosednjih