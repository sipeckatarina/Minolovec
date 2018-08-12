# tukaj je leđit koda ... v nastajanju

import tkinter as tk
import gumbi as g



okno = tk.Tk()
okno.title('Minolovec (upam)')
okno.geometry("500x500") #You want the size of the app to be 500x500
okno.resizable(0, 0) #Don't allow resizing in the x or y direction

zg = tk.Frame(okno)
sp = tk.Frame(okno)
zg.pack()
sp.pack()

zgornji_napis = tk.Label(zg, text='Tukaj pride kup enih izmišljotin...')
zgornji_napis.pack()


#okno.option_add("*Button.Background", "black")
#okno.option_add("*Button.Foreground", "red")
#gumb = tk.Button(okno, text='to je gumb')


okno.mainloop()