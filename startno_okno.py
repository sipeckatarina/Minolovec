import tkinter as tk


class Konstanta():
    def __init__(self, stevilo):
        self.stevilo = stevilo

VRSTICE = Konstanta(10)
STOLPCI = Konstanta(10)
BOMBE = Konstanta(int(VRSTICE.stevilo * STOLPCI.stevilo * 0.1))


def preveri():
    vrstice = vhod_vrstice.get()
    stolpci = vhod_stolpci.get()
    bombe = vhod_bombe.get()
    if vrstice == '':
        vrstice = str(VRSTICE.stevilo)
    if stolpci == '':
        stolpci = str(STOLPCI.stevilo)
    if bombe == '':
        bombe = str(BOMBE.stevilo)
    vse = vrstice + stolpci + bombe
    if preveri_digit(vse):
        if preveri_stevilo_bomb(vrstice, stolpci, bombe):
            if preveri_velikost(vrstice, stolpci):
                VRSTICE.stevilo = int(vrstice)
                STOLPCI.stevilo = int(stolpci)
                BOMBE.stevilo = int(bombe)


def preveri_digit(vse):
    if not vse.isdigit():
        napisi_opozorilo('digit')
        return False
    return True


def preveri_stevilo_bomb(vrstice, stolpci, bombe):
    if int(vrstice) * int(stolpci) < int(bombe):
        napisi_opozorilo('bombe')
        return False
    return True


def preveri_velikost(vrstice, stolpci):
    if int(vrstice) < 5 or int(vrstice) > 35:
        napisi_opozorilo('vrstice')
        return False
    if int(stolpci) < 5 or int(stolpci) > 35:
        napisi_opozorilo('stolpci')
        return False
    return True


def napisi_opozorilo(thing):
    if thing == 'digit':
        opozorilo.config(text='Prosim, vpišite le naravna števila ali pustite prazno.')
    elif thing == 'bombe':
        opozorilo.config(text='Število bomb presega število polj.')
    elif thing == 'vrstice':
        opozorilo.config(text='Število vrstic naj bo vsaj 5 in manjše od 36.')
    else:
        opozorilo.config(text='Število stolpcev naj bo vsaj 5 in manjše od 36.')
    opozorilo.grid(row=3, column=1)


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


def ok():
    preveri()
    opozorilo.config(text='Hvala! ;)', fg='black')
    opozorilo.grid(row=3, column=1)
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
opozorilo = tk.Label(spodaj, text='', fg='red')

#OK
ok_button = tk.Button(okno, text='OK', command=ok)
ok_button.grid(row=6, column=1)


okno.mainloop()