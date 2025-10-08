import tkinter as tk
from tkinter import *
import random as rd

versuche = 0
number = rd.randint(1,100)

def abgleich():
    global versuche
    if number == int(eingabebox.get()):
        versuche = versuche+1
        ausgabe.config(text="Richtig Geraten")
        versuche_label.config(text=f"Du hast {versuche} Versuch(e) gebraucht")
    elif number > int(eingabebox.get()):
        versuche = versuche+1
        ausgabe.config(text="Die Zahl ist Größer")
    else:
        versuche = versuche+1
        ausgabe.config(text="Die Zahl ist Kleiner")

main = tk.Tk()
main.title("Guess the Number")
main.geometry("300x200")
main.resizable(width=False,
               height=False,
               )

title = tk.Label(main,
                 text="Gib Deinen Tipp ein",
                 )
title.place(relx=0.5,
            rely=0.2,
            anchor="center",
            )
number_range = tk.Label(main,
                        text="Die Nummer kann 1 bis 100 Sein")
number_range.place(relx=0.5,
                   rely=0.3,
                   anchor="center",
                   )
eingabebox = tk.Entry(main,
                      justify="center",
                      )
eingabebox.place(relx=0.5,
                 rely=0.4,
                 anchor="center",
                 )
eingabe_button = tk.Button(main,
                           text="Guess",
                           command=abgleich,
                           )
eingabe_button.place(relx=0.5,
                     rely=0.55,
                     anchor="center",
                     )
ausgabe = tk.Label(main,
                   )
ausgabe.place(relx=0.5,
              rely=0.7,
              anchor="center",
              )
versuche_label = tk.Label(main,
                          )
versuche_label.place(relx=0.5,
                     rely=0.8,
                     anchor="center",
                     )

main.mainloop()