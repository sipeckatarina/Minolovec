# tukaj je leđit koda ... v nastajanju
import tkinter as tk
import startno_okno as sto
#import gumbi as g
#from gumbi import Gumb

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

class Gumb():

    def __init__(self, vrstica, stolpec, stevilka=None, stanje=0, okno=sp):
        #stanje 0 = nepritisnjen, stanje 1 je pritisnjen
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.stanje = stanje
        self.stevilka = stevilka
        self.velikost = VELIKOST_GUMBA
        self.button = tk.Button(okno, text='', width=self.velikost, height=self.velikost//2, command=self.levi_klik)

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

    def levi_klik(self):
        self.button.config(text='{}'.format(self.stevilka))

#    def postavi_zastavico:



############################################################################################################################


#mreža z gumbi
for i in range(VRSTICE):
    for j in range(STOLPCI):
        Gumb(i, j, (i + j)%9).prikazi(sp)

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

gumb_za_zastavico = tk.Button(sp, text='BOMBA', height=VELIKOST_GUMBA//2, width=VELIKOST_GUMBA)#, command=naredi_zastavico)
gumb_za_zastavico.grid(row=VRSTICE+2, column=STOLPCI//2)

main_okno.mainloop()