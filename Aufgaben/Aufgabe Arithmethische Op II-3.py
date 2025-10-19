# Lebensmittel

print("")
Anzahl_Aepfel = int(input("Bitte geben sie die Anzahl der Äpfel an: "))
Preis_Aepfel = float(input("Bitte geben sie den Preis für einen Apfel an: "))

Anzahl_Bananen = int(input("Bitte geben sie die Anzahl der Bananen an: "))
Preis_Bananen = float(input("Bitte geben sie den Preis für eine Banane an: "))

Anzahl_Orangen = int(input("Bitte geben sie die Anzahl der Orangen an: "))
Preis_Orangen = float(input("Bitte geben sie den Preis für eine Orange an: "))

Gesamt_Aepfel = Anzahl_Aepfel*Preis_Aepfel
Gesamt_Bananen = Anzahl_Bananen*Preis_Bananen
Gesamt_Orangen = Anzahl_Orangen*Preis_Orangen
Gesamt_Einkauf = Gesamt_Aepfel+Gesamt_Bananen+Gesamt_Orangen

print("")
print(f"Die Äpfel kosten: {Gesamt_Aepfel:.2f} Euro")
print(f"Die Bananen kosten: {Gesamt_Bananen:.2f} Euro")
print(f"Die Orangen kosten: {Gesamt_Orangen:.2f} Euro")
print(f"Der Gesamte Einkauf kostet: {Gesamt_Einkauf:.2f} Euro")
print("")
