import random as rd
try: 
    eingabe = float(input("Bitte eine Zahl von 1 bis 10 mit einer Nachkommastelle an"))
    if eingabe >= float(1.0) and eingabe <= float(10.9):
        zahl = round(rd.uniform(1,10),1)
        if eingabe == zahl:
            print("Sie haben gewonnen!!!")
        else:
            print(f"Leider verloren! die Zahl war {zahl}")
    else:
        print("Bitte im Bereich 1.0-10.9")
except ValueError:
    print("Nur Zahlen")
