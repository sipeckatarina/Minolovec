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
                        par[0] = par[0][2:]
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

    def __init__(self, ime, rezultat, dopisi=False):

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

        #dejanski rezultati
        self.dodaj_rezultat()
        self.rezultati = preberi()
        self.napisi_rezultate()

        self.okno.mainloop()

    def napisi_rezultate(self):
        rez = self.rezultati
        for i in range(12):
            tk.Label(self.sredina, text=str(rez[i][0])).grid(row=i+2, column=1)
            tk.Label(self.sredina, text=str(rez[i][1])).grid(row=i+2, column=2)

    def dodaj_rezultat(self):
        if self.dopisi:
            with open('rezultati.txt', 'a') as dat_rezultati:
                print('-> {}, {}'.format(self.ime, self.rezultat), file=dat_rezultati)
