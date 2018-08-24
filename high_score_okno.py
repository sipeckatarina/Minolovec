import tkinter as tk


def preberi():

    with open('rezultati.txt') as dat:
        dat_rezultati = []
        for vrstica in dat:
            dat_rezultati.append(vrstica)
        rezultati = []
        for rezultat in dat_rezultati:
            par = rezultat.split(', ')
            if rezultat != dat_rezultati[-1]:
                if len(par[0]) > 3:
                    if par[0][0:2] == '->':
                        par[0] = par[0][3:]
            ime = par[0]
            tocke = int(par[1])
            if (ime, tocke) not in rezultati:
                rezultati.append((ime, tocke))
    rezultati.sort(key=lambda r: r[1])
    rezultati = rezultati[::-1]
    if len(rezultati) < 12:
        for mesto in range(12 - len(rezultati)):
            rezultati.append(('', ''))
    return rezultati


class High_score_okno():

    def __init__(self, ime, rezultat, dopisi='ne'):

        self.dopisi = dopisi
        self.rezultat = rezultat
        self.ime = ime

        #okno
        self.okno = tk.Tk()
        self.okno.title('Minolovec')

        #razdeljeno okno na tri dele
        self.zgoraj = tk.Frame(self.okno)
        self.sredina = tk.Frame(self.okno)
        self.spodaj = tk.Frame(self.okno)
        self.zgoraj.grid(row=1, column=1)
        self.sredina.grid(row=2, column=1)
        self.spodaj.grid(row=3, column=1)

        #zgornji napis
        tk.Label(self.zgoraj, text=' Najvišji rezultati:', fg='Blue2').grid(row=1, column=1)

        #prazna vrstica
        self.prazna_vrstica = tk.Label(self.zgoraj)
        self.prazna_vrstica.grid(row=2, column=1)

        #napisa za rezultat (ime in tocke)
        tk.Label(self.sredina, text='IME:', fg='VioletRed1').grid(row=1, column=1)
        tk.Label(self.sredina, text='TOČKE:     ', fg='VioletRed1').grid(row=1, column=2)

        #nastavki za rezultate
        self.prvi_ime = tk.Label(self.sredina, text='')
        self.drugi_ime = tk.Label(self.sredina, text='')
        self.tretji_ime = tk.Label(self.sredina, text='')
        self.cetrti_ime = tk.Label(self.sredina, text='')
        self.peti_ime = tk.Label(self.sredina, text='')
        self.sesti_ime = tk.Label(self.sredina, text='')
        self.sedmi_ime = tk.Label(self.sredina, text='')
        self.osmi_ime = tk.Label(self.sredina, text='')
        self.deveti_ime = tk.Label(self.sredina, text='')
        self.deseti_ime = tk.Label(self.sredina, text='')
        self.enajsti_ime = tk.Label(self.sredina, text='')
        self.dvanajsti_ime = tk.Label(self.sredina, text='')
        self.prvi_tocke = tk.Label(self.sredina, text='')
        self.drugi_tocke = tk.Label(self.sredina, text='')
        self.tretji_tocke = tk.Label(self.sredina, text='')
        self.cetrti_tocke = tk.Label(self.sredina, text='')
        self.peti_tocke = tk.Label(self.sredina, text='')
        self.sesti_tocke = tk.Label(self.sredina, text='')
        self.sedmi_tocke = tk.Label(self.sredina, text='')
        self.osmi_tocke = tk.Label(self.sredina, text='')
        self.deveti_tocke = tk.Label(self.sredina, text='')
        self.deseti_tocke = tk.Label(self.sredina, text='')
        self.enajsti_tocke = tk.Label(self.sredina, text='')
        self.dvanajsti_tocke = tk.Label(self.sredina, text='')

        self.prvi_ime.grid(row=3, column=1)
        self.drugi_ime.grid(row=4, column=1)
        self.tretji_ime.grid(row=5, column=1)
        self.cetrti_ime.grid(row=6, column=1)
        self.peti_ime.grid(row=7, column=1)
        self.sesti_ime.grid(row=8, column=1)
        self.sedmi_ime.grid(row=9, column=1)
        self.osmi_ime.grid(row=10, column=1)
        self.deveti_ime.grid(row=11, column=1)
        self.deseti_ime.grid(row=12, column=1)
        self.enajsti_ime.grid(row=13, column=1)
        self.dvanajsti_ime.grid(row=14, column=1)
        self.prvi_tocke.grid(row=3, column=2)
        self.drugi_tocke.grid(row=4, column=2)
        self.tretji_tocke.grid(row=5, column=2)
        self.cetrti_tocke.grid(row=6, column=2)
        self.peti_tocke.grid(row=7, column=2)
        self.sesti_tocke.grid(row=8, column=2)
        self.sedmi_tocke.grid(row=9, column=2)
        self.osmi_tocke.grid(row=10, column=2)
        self.deveti_tocke.grid(row=11, column=2)
        self.deseti_tocke.grid(row=12, column=2)
        self.enajsti_tocke.grid(row=13, column=2)
        self.dvanajsti_tocke.grid(row=14, column=2)

        self.dodaj_rezultat()
        self.rezultati = preberi()
        self.napisi_rezultate()

        self.okno.mainloop()

    def napisi_rezultate(self):
        self.prvi_ime.config(text=str(self.rezultati[0][0]))
        self.drugi_ime.config(text=str(self.rezultati[1][0]))
        self.tretji_ime.config(text=str(self.rezultati[2][0]))
        self.cetrti_ime.config(text=str(self.rezultati[3][0]))
        self.peti_ime.config(text=str(self.rezultati[4][0]))
        self.sesti_ime.config(text=str(self.rezultati[5][0]))
        self.sedmi_ime.config(text=str(self.rezultati[6][0]))
        self.osmi_ime.config(text=str(self.rezultati[7][0]))
        self.deveti_ime.config(text=str(self.rezultati[8][0]))
        self.deseti_ime.config(text=str(self.rezultati[9][0]))
        self.enajsti_ime.config(text=str(self.rezultati[10][0]))
        self.dvanajsti_ime.config(text=str(self.rezultati[11][0]))

        self.prvi_tocke.config(text=str(self.rezultati[0][1]))
        self.drugi_tocke.config(text=str(self.rezultati[1][1]))
        self.tretji_tocke.config(text=str(self.rezultati[2][1]))
        self.cetrti_tocke.config(text=str(self.rezultati[3][1]))
        self.peti_tocke.config(text=str(self.rezultati[4][1]))
        self.sesti_tocke.config(text=str(self.rezultati[5][1]))
        self.sedmi_tocke.config(text=str(self.rezultati[6][1]))
        self.osmi_tocke.config(text=str(self.rezultati[7][1]))
        self.deveti_tocke.config(text=str(self.rezultati[8][1]))
        self.deseti_tocke.config(text=str(self.rezultati[9][1]))
        self.enajsti_tocke.config(text=str(self.rezultati[10][1]))
        self.dvanajsti_tocke.config(text=str(self.rezultati[11][1]))

    def dodaj_rezultat(self):
        if self.dopisi == 'ja':
            with open('rezultati.txt', 'a') as dat_rezultati:
                print('-> {}, {}'.format(self.ime, self.rezultat), file=dat_rezultati)

#High_score_okno('Anže', 200)