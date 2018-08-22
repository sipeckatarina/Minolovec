import tkinter as tk


class Konstanta():
    def __init__(self, stevilo):
        self.stevilo = stevilo

#v mainu VRSTICE, STOLPCI in BOMBE niso objekti, ampak stevila
VRSTICE = Konstanta(15)
STOLPCI = Konstanta(15)
BOMBE = Konstanta(0)


class Startno_okno():

    def __init__(self):

        #okno
        self.okno = tk.Tk()
        self.okno.title('Minolovec')

        #poravnaj okno
        #self.sirina_okna = self.okno.winfo_reqwidth()
        #self.dolzina_okna = self.okno.winfo_reqheight()
        #self.sirina_ekrana = self.okno.winfo_screenwidth()
        #self.dolzina_ekrana = self.okno.winfo_screenheight()
        #self.pozicija_desno = int(self.sirina_ekrana / 2 - self.sirina_okna / 2)
        #self.pozicija_dol = int(self.dolzina_ekrana / 2 - self.dolzina_okna / 2)
        #self.okno.geometry("+{}+{}".format(self.pozicija_desno, self.pozicija_dol))

        #razdeljeno okno na tri dele
        self.cist_zgoraj = tk.Frame(self.okno)
        self.zgoraj = tk.Frame(self.okno)
        self.spodaj = tk.Frame(self.okno)
        self.cist_zgoraj.grid(row=1, column=1)
        self.zgoraj.grid(row=2, column=1)
        self.spodaj.grid(row=3, column=1)

        #definirani napisi
        pri='Privzete vrednosti so {}, {} in {}.'.format(VRSTICE.stevilo, STOLPCI.stevilo, BOMBE.stevilo)
        self.napis_privzeto = tk.Label(self.cist_zgoraj, text=pri, fg='grey')
        self.napis_vhod_vrstice = tk.Label(self.zgoraj, text='Število vrstic: ')
        self.napis_vhod_stolpci = tk.Label(self.zgoraj, text='Število stolpcev: ')
        self.napis_vhod_bombe = tk.Label(self.zgoraj, text='Število bomb: ')
        self.napis_vhod_ime = tk.Label(self.zgoraj, text='Vaše ime: ')

        #definirani vhodi
        self.vhod_vrstice = tk.Entry(self.zgoraj)
        self.vhod_stolpci = tk.Entry(self.zgoraj)
        self.vhod_bombe = tk.Entry(self.zgoraj)
        self.vhod_ime = tk.Entry(self.zgoraj)

        #zgornji del
        self.napis_privzeto.grid(row=1, column=1)
        self.napis_vhod_ime.grid(row=1, column=1)
        self.napis_vhod_vrstice.grid(row=2, column=1)
        self.napis_vhod_stolpci.grid(row=3, column=1)
        self.napis_vhod_bombe.grid(row=5, column=1)
        self.vhod_ime.grid(row=1, column=2)
        self.vhod_vrstice.grid(row=2, column=2)
        self.vhod_stolpci.grid(row=3, column=2)
        self.vhod_bombe.grid(row=5, column=2)

        #priporoci
        self.priporoci_gumb = tk.Button(self.spodaj, text='priporoči število bomb', command=self.priporoci)
        self.priporoci_gumb.grid(row=2, column=1)

        #prazna vrstica, da je lepše
        self.prazna_vrstica = tk.Label(text=' ')
        self.prazna_vrstica.grid(row=5, column=1)

        #opozorila
        self.opozorilo = tk.Label(self.spodaj, text='', fg='red')

        #hvala
        self.hvala = tk.Label(self.spodaj, text='')

        #OK
        self.ok_button = tk.Button(self.okno, text='OK', command=self.ok)
        self.ok_button.grid(row=6, column=1)

        self.okno.mainloop()

    def preveri(self):
        vrstice = self.vhod_vrstice.get()
        stolpci = self.vhod_stolpci.get()
        bombe = self.vhod_bombe.get()
        if vrstice == '':
            vrstice = str(VRSTICE.stevilo)
        if stolpci == '':
            stolpci = str(STOLPCI.stevilo)
        if bombe == '':
            bombe = str(BOMBE.stevilo)
        vse = vrstice + stolpci + bombe
        if self.preveri_digit(vse):
            if self.preveri_stevilo_bomb(vrstice, stolpci, bombe):
                if self.preveri_velikost(vrstice, stolpci):
                    VRSTICE.stevilo = int(vrstice)
                    STOLPCI.stevilo = int(stolpci)
                    BOMBE.stevilo = int(bombe)
                    self.opozorilo.config(text='')
                    self.hvala.config(text='Hvala.')
                    self.hvala.grid(row=3, column=1)
                    return True
        return False

    def preveri_digit(self, vse):
        if not vse.isdigit():
            self.napisi_opozorilo('digit')
            return False
        return True

    def preveri_stevilo_bomb(self, vrstice, stolpci, bombe):
        if int(vrstice) * int(stolpci) < int(bombe):
            self.napisi_opozorilo('bombe')
            return False
        return True

    def preveri_velikost(self, vrstice, stolpci):
        if int(vrstice) < 5 or int(vrstice) > 25:
            self.napisi_opozorilo('vrstice')
            return False
        if int(stolpci) < 5 or int(stolpci) > 25:
            self.napisi_opozorilo('stolpci')
            return False
        return True

    def napisi_opozorilo(self, thing):
        if thing == 'digit':
            self.opozorilo.config(text='Prosim, vpišite le naravna števila ali pustite prazno.')
        elif thing == 'bombe':
            self.opozorilo.config(text='Število bomb presega število polj.', fg='red')
        elif thing == 'vrstice':
            self.opozorilo.config(text='Število vrstic naj bo vsaj 5 in manjše ali enako 25.')
        else:
            self.opozorilo.config(text='Število stolpcev naj bo vsaj 5 in manjše ali enako 25.')
        self.opozorilo.grid(row=3, column=1)
        self.hvala.config(text='')

    def priporoci(self):
        self.preveri()
        if self.preveri():
            vrstice = VRSTICE.stevilo
            stolpci = STOLPCI.stevilo
            if self.vhod_vrstice.get() != '':
                vrstice = int(self.vhod_vrstice.get())
            if self.vhod_stolpci.get() != '':
                stolpci = int(self.vhod_stolpci.get())
            priporocilo = (int(vrstice * stolpci * 0.15))
            napis_priporocilo_bombe = tk.Label(self.spodaj, text='priporočeno število bomb: {}'.format(priporocilo))
            napis_priporocilo_bombe.grid(row=1, column=1)
            BOMBE.stevilo = priporocilo

    def ok(self):
        self.name = self.vhod_ime.get()
        if len(self.name) > 0:
            self.ime = self.name[0].upper() + self.name[1:]
        else:
            self.ime = 'Boštjan'
        self.preveri()
        if self.preveri():
            if BOMBE.stevilo == 0:
                BOMBE.stevilo = int(VRSTICE.stevilo * STOLPCI.stevilo * 0.15)
            self.hvala.config(text='Hvala! ;)')
            self.hvala.grid(row=3, column=1)
            print('Izbrano ime: ', self.ime)
            print('Izbrano stevilo vrstic: ', VRSTICE.stevilo)
            print('Izbrano stevilo stolpcev: ', STOLPCI.stevilo)
            print('Izbrano stevilo bomb: ', BOMBE.stevilo)
            self.okno.destroy()

#Startno_okno()