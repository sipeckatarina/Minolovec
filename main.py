# tukaj je leđit koda ... v nastajanju
import tkinter as tk
#import gumbi as g
#from gumbi import Gumb

VRSTICE, STOLPCI = 10, 10
BOMBE = int(VRSTICE * STOLPCI * 0.1)

okno = tk.Tk()
okno.title('Minolovec (upam)')
okno.geometry("500x500") #velikost okna

#razdeljeno okno na dva dela
zg = tk.Frame(okno)
sp = tk.Frame(okno)
zg.pack()
sp.pack()

#zgornji napisi za stevilo vrstic, stolpcev in bomb
zgornji_napis_vrstice = tk.Label(zg, text='Število vrstic: {}'.format(VRSTICE))
zgornji_napis_stolpci = tk.Label(zg, text='Število stolpcev: {}'.format(STOLPCI))
zgornji_napis_bombe = tk.Label(zg, text='Število bomb: {}'.format(BOMBE))
zgornji_napis_vrstice.pack()
zgornji_napis_stolpci.pack()
zgornji_napis_bombe.pack()



class Gumb():

    def __init__(self, stanje=0, stevilka=None):
        #stanje 0 = nepritisnjen, stanje 1 je pritisnjen
        #self.vrstica = vrstica
        #self.stolpec = stolpec
        self.stanje = stanje
        self.stevilka = stevilka

    def __repr__(self):
        return 'Gumb ({}, {}, {}, {})'.format(self.vrstica, self.stolpec, self.stanje, self.stevilka)

    def __str__(self):
        stan = 5
        if self.stanje == 0:
            stan = 'nepritisnjen'
        else: stan = 'pritisnjen'
        return 'Gumb na ({0}, {1}), '.format(self.vrstica, self.stolpec) + stan + ' s stevilko {}.'.format(self.stevilka)


gumb = [[Gumb() for i in range(STOLPCI)] for j in range(VRSTICE)]


#koda za mrežo z gumbi
for i in range(VRSTICE):
    for j in range(STOLPCI):
        b = gumb[i][j]
        tk.Button(sp, height = int(29/VRSTICE), width = int(45/STOLPCI)).grid(row=i, column=j)

'''
button1.config( height = WHATEVER, width = WHATEVER2 )
button1 = Button(self, text = "Send", command = self.response1, height = 100, width = 100)
'''

#okno = tk.Tk()
#vhod = tk.Entry(okno)
#gumb = tk.Button(okno, text='text', command=odzdravi)
#okno.option_add("*Button.Background", "black")
#okno.option_add("*Button.Foreground", "red")


okno.mainloop()