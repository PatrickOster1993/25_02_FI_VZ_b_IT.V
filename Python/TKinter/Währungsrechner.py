#Import der tkinter Library für GUI
import tkinter as tk
from tkinter import *

#Checkbox Funktion
def checked():
    if checkvar.get() == True:
        label1.config(text="USD/EUR")
        entry_usd.config(state="normal")
        entry_eur.config(state="readonly")
    else:
        label1.config(text="EUR/USD")
        entry_eur.config(state="normal")
        entry_usd.config(state="readonly")

#Berechnung
def rechnen():
    if checkvar.get() == False:
        eur = float(entry_eur.get())
        kurs_eur = 1.17
        ergebnis_usd = round(eur*kurs_eur,2)        
        entry_eur.delete(0,END)
        entry_usd.config(state="normal")
        entry_usd.insert(0,ergebnis_usd)
        entry_usd.config(state="readonly")
    else:
        usd = float(entry_usd.get())
        kurs_usd = 0.85
        ergebnis_eur = round(usd*kurs_usd,2)
        entry_usd.delete(0,END)
        entry_eur.config(state="normal")
        entry_eur.insert(0,ergebnis_eur)
        entry_eur.config(state="readonly")

#Hauptfenster
root = tk.Tk()

root.title("Währungsrechner")
root.geometry("300x200")
root.resizable(width=False, 
               height=False)

#GUI
#Umschalten Checkbox
checkvar = BooleanVar()
checkbox = tk.Checkbutton(root, 
                          onvalue=True, 
                          offvalue=False, 
                          variable=checkvar, 
                          command=checked, 
                          text="Umschalten", 
                          compound="left")
checkbox.place(x=130, 
               y=38)

label1 = tk.Label(root, 
                  text="EUR/USD")
label1.place(x=75, 
             y=40)

#Berechnen Button
berechnen = tk.Button(root,
                      text="Berechnen",
                      command=rechnen)
berechnen.place(x=80,
                y=130)

#Beenden Button
beenden = tk.Button(root, 
                    text="Quit",
                    command=quit)
beenden.place(x=160,
              y=130)

#Überschrift
ueberschrift = tk.Label(root, 
                        text="Rechner für EUR und USD")
ueberschrift.place(x = 75,
                   y = 10)

#Eingabefeld Euro
entry_eur = tk.Entry(root)
entry_eur.place(x=75,
                y=60)
label_eur = tk.Label(root,
                     text="EUR")
label_eur.place(x=200,
                y=60)

#Eingabefeld USD
entry_usd = tk.Entry(root,
                     state="readonly")
entry_usd.place(x=75,
                y=80)
label_usd = tk.Label(root,
                     text="USD")
label_usd.place(x=200,
                y=80)

root.mainloop()