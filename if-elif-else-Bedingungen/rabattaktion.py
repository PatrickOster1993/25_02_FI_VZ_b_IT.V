warnekorb_wert=float(input("Wie hoch ist der Warenkorbwert ? "))
if warnekorb_wert>=50:
    rabatt_wert=warnekorb_wert-warnekorb_wert*0.1
    print(f"Der Warenkorbwert beträgt {warnekorb_wert:.2f} €, Sie erhalten 10% Rabatt, somit beträgt der Endpreis {rabatt_wert:.2f} €")
else:
    print(f"Der Warenkorbwert beträgt {warnekorb_wert:.2f} €, leider erhalten Sie keinen Rabatt!")