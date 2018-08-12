import tkinter as tk

class Gumb():

    def __init__(self, vrstica, stolpec, stanje=0, stevilka=None):
        #stanje 0 = nepritisnjen, stanje 1 je pritisnjen
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.stanje = stanje
        self.stevilka = stevilka

    def __str__(self):
        stan = 5
        if self.stanje == 0:
            stan = 'nepritisnjen'
        else: stan = 'pritisnjen'
        return 'Gumb na ({0}, {1}), '.format(self.vrstica, self.stolpec) + stan + ' s stevilko {}.'.format(self.stevila)
