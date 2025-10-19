# Rabatt

# Voraussetzung: zwei Erwachsene und ein Kind

aufenthaltsdauer = input("\nBitte geben sie die Anzahl der Nächte an die sie bleiben wollen: ")
alter_kind = input("\nBitte geben sie das Alter ihres Kindes in Jahren an: ")

zimmerpreis = 150

if aufenthaltsdauer.isdigit() and alter_kind.isdigit():
    aufenthaltsdauer = int(aufenthaltsdauer)
    alter_kind = int(alter_kind)

    if alter_kind < 7:
        rabatt = 100
    elif alter_kind >= 7 and alter_kind < 18:
        rabatt = 70
    else:
        rabatt = 0
else:
    print("\nDas war keine gültige Eingabe, bitte versuchen sie es später noch einmal")
    print("\n")
    quit()

kinderpreis = zimmerpreis*aufenthaltsdauer*(1-rabatt/100)
erwachsenenpreis = zimmerpreis*aufenthaltsdauer

print(f"\nDer Preis für ihren Aufenthalt beträgt: {2*erwachsenenpreis+kinderpreis} Euro")
print("\n")
