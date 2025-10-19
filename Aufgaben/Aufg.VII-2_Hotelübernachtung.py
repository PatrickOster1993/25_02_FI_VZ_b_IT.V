# Hotelübernachtung

anzahl_person = input("\nWieviele Personen sind sie?: ")
aufenthaltsdauer = input("\nWieviele Nächte wollen sie bleiben?: ")

zimmerpreis = 70
Mwst = 1.19


if anzahl_person.isdigit() and aufenthaltsdauer.isdigit():
    anzahl_person = int(anzahl_person)
    aufenthaltsdauer= int(aufenthaltsdauer)
    nettobetrag = zimmerpreis*aufenthaltsdauer*anzahl_person
    gesamtpreis = nettobetrag*Mwst
    
    if aufenthaltsdauer == 1 and anzahl_person != 0:
        print(f"\nDie Gesamtkosten betragen somit: {(nettobetrag+20)*Mwst:.2f} Euro")
        print("\n")
    else:
        print(f"\nDie Gesamtkosten betragen somit: {gesamtpreis} Euro")
        print("\n")
else:
    print("\nFehlerhafte eingabe, bitte geben sie nur ganze zahlen ein!")
    print("\n")
    
