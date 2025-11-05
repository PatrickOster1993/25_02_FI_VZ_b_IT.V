punktezahl=int(input("Erreichte Punktezahl: "))

if punktezahl<=100 and punktezahl>=90:
    print(f"Herzlichen Glückwunsch du hast die Note 1, mit {punktezahl} Punkten !")
elif punktezahl <=89 and punktezahl>=80:
    print(f"Super....du hast die Note 2, mit {punktezahl} Punkten !")
elif punktezahl<=79 and punktezahl>=70:
    print(f"Ein befriedigendes Ergebnis, du hast die Note 3, mit {punktezahl} Punkten !")  
elif punktezahl<=69 and punktezahl>=60:
    print(f"Noch aussreichend, du hast die Note 4, mit {punktezahl} Punkten ! Das kannst du besser !!!")  
elif punktezahl<=59 and punktezahl>=0: 
    print(f"Suche dir dringend Hilfe, du hast die Note 5, mit {punktezahl} Punkten ! Schäm dich !!")   
else:
    print("Du hast einen falschen Zahlenwert eingegeben!")