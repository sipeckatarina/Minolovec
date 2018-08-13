import tkinter as tk


class Konstanta():
    def __init__(self, stevilo):
        self.stevilo = stevilo

VRSTICE = Konstanta(10)
STOLPCI = Konstanta(10)
BOMBE = Konstanta(int(VRSTICE.stevilo * STOLPCI.stevilo * 0.1))


def priporoci():
    preveri()
    vrstice = VRSTICE.stevilo
    stolpci = STOLPCI.stevilo
    if vhod_vrstice.get() != '' and vhod_vrstice.get().isdigit():
        vrstice = int(vhod_vrstice.get())
    if vhod_stolpci.get() != '' and vhod_stolpci.get().isdigit():
        stolpci = int(vhod_stolpci.get())
    napis_priporocilo_bombe = tk.Label(spodaj, text='priporočeno število bomb: {}'.format(str(int(vrstice * stolpci // 10))))
    napis_priporocilo_bombe.grid(row=1, column=1)


def preveri():
    vse_je_ok = 1 #da na koncu vemo, ce se kaj naredi ali pa vse porpade
    vrstice = vhod_vrstice.get()
    stolpci = vhod_stolpci.get()
    bombe = vhod_bombe.get()
    vse = vrstice + stolpci + bombe
    if not(vse.isdigit() or (vse == '')):
        vse_je_ok = 0
        napisi_opozorilo_ni_naravno_stevilo('ja')
    if vse_je_ok == 1:
        if vrstice != '':
            VRSTICE.stevilo = int(vrstice)
        if stolpci != '':
            STOLPCI.stevilo = int(stolpci)
        napisi_opozorilo_ni_naravno_stevilo('ne')
        if bombe != '':
            if VRSTICE.stevilo * STOLPCI.stevilo < int(bombe):
                napisi_opozorilo_prevec_bomb('ja')
            else:
                napisi_opozorilo_prevec_bomb('ne')
                BOMBE.stevilo = int(bombe)
        napisi_opozorilo_ni_naravno_stevilo('ne')


def napisi_opozorilo_ni_naravno_stevilo(mogoce):
    if mogoce == 'ja':
        ni_naravno_stevilo.config(text='Prosim, vpišite le naravna števila ali pa pustite prazno.')
        ni_naravno_stevilo.config(fg='red')
        ni_naravno_stevilo.grid(row=3, column=1)
    else:
        ni_naravno_stevilo.config(text='Hvala! ;)')
        ni_naravno_stevilo.config(fg='black')
        ni_naravno_stevilo.grid(row=3, column=1)


def napisi_opozorilo_prevec_bomb(mogoce):
    if mogoce == 'ja':
        prevec_bomb.config(text='Število bomb presega število polj. To ni kul.')
        prevec_bomb.config(fg='red')
        prevec_bomb.grid(row=4, column=1)
    else:
        prevec_bomb.config(text='')
        prevec_bomb.grid(row=4, column=1)


def ok():
    preveri()
    print('Izbrano stevilo vrstic: ', VRSTICE.stevilo)
    print('Izbrano stevilo stolpcev: ', STOLPCI.stevilo)
    print('Izbrano stevilo bomb: ', BOMBE.stevilo)


#####################################################################################################################


#okno
okno = tk.Tk()
okno.title('Minolovec (upam)')

#razdeljeno okno na dva dela
zgoraj = tk.Frame(okno)
spodaj = tk.Frame(okno)
zgoraj.grid(row=1, column=1)
spodaj.grid(row=2, column=1)

#definirani napisi
napis_vhod_vrstice = tk.Label(zgoraj, text='Število vrstic: ')
napis_vhod_stolpci = tk.Label(zgoraj, text='Število stolpcev: ')
napis_vhod_bombe = tk.Label(zgoraj, text='Število bomb: ')

#definirani vhodi
vhod_vrstice = tk.Entry(zgoraj)
vhod_stolpci = tk.Entry(zgoraj)
vhod_bombe = tk.Entry(zgoraj)

#zgornji del
napis_vhod_vrstice.grid(row=1, column=1)
napis_vhod_stolpci.grid(row=3, column=1)
napis_vhod_bombe.grid(row=5, column=1)
vhod_vrstice.grid(row=1, column=2)
vhod_stolpci.grid(row=3, column=2)
vhod_bombe.grid(row=5, column=2)

#priporoci
priporoci_gumb = tk.Button(spodaj, text='priporoči', command=priporoci)
priporoci_gumb.grid(row=2, column=1)

#prazna vrstica, da je lepše
prazna_vrstica = tk.Label(text=' ')
prazna_vrstica.grid(row=5, column=1)

#opozorila
ni_naravno_stevilo = tk.Label(spodaj, text='', fg='red')
prevec_bomb = tk.Label(spodaj, text='')

#OK
ok_button = tk.Button(okno, text='OK', command=ok)
ok_button.grid(row=6, column=1)


okno.mainloop()