# Aufgabe 2: Lagerbestand prüfen

produkte = [("Bleistift", 30), ("Heft", 60), ("Radiergummi", 20), ("Marker", 80)]

for produkt, bestand in produkte:
    if bestand < 50:
        print(f"\nDas Produkt [{produkt}] muss nachbestellt werden!")
print()
