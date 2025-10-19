#  Angebot für Hotelübernachtungen

print("")
anzahl_personen = int(input("Bitte geben sie die Anzahl der Personen ein: "))
Aufenhaltsdauer = int(input("Bitte geben sie die Anzahl der Tage ihres Aufenthaltes an: "))

Zimmerpreis = 70
Nettopreis = Zimmerpreis*Aufenhaltsdauer*anzahl_personen
Gesamtpreis = Nettopreis*1.19

print("")
print(f"Das ergibt einen Gesamtpreis von: {Gesamtpreis} Euro")
print("")