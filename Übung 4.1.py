print("Warenwert eintagen")
warenwert=input()

eingabe=int(warenwert)
if eingabe>=50:
    print(eingabe*0.9)
if eingabe<=50:
    print("Leider kein Rabatt")