#Aufgabe 2 Aufschlag

zimmerpreis = 70
mwst = 0.19
aufschlag = 20

def berechnung():
    netto_preis = zimmerpreis*anzahl_personen*aufendhaltsdauer
    return netto_preis

def brutto(netto):
    brutto_preis = netto*(1+mwst)
    return brutto_preis

print(f"Willkommen in unserem Hotel.\nUnser Zimmerpreis beträgt {zimmerpreis}€ pro Person\nBei nur einer Übernachtung berechnen wir eine kleine zusatz Gebühr\nWir danken für Ihr Verständniss\nBitte geben Sie die Personen Anzahl ein")

while True:
    try:
        anzahl_personen = int(input())
        print("Bitte geben Sie die Aufendhaltsdauer an")
        aufendhaltsdauer = int(input())
        break
    except ValueError:
        print("Nur Ganze Zahlen eingeben")

if aufendhaltsdauer == 1:
    gesamt = brutto(berechnung()+aufschlag)
    print(f"Ihr Gesamtbetrag lautet {gesamt:.2f}€")
else:
    gesamt = brutto(berechnung())
    print(f"Ihr Gesamtbetrag lautet {gesamt:.2f}€")
