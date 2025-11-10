# Die drei Produkt-Dictionaries erstellen
produkt_1 = {
    "produkt_id": 101,
    "name": "SSD 1TB",
    "lagerbestand": 35
}
produkt_2 = {
    "produkt_id": 102,
    "name": "Gaming-Maus",
    "lagerbestand": 15
}
produkt_3 = {
    "produkt_id": 103,
    "name": "24 Zoll Monitor",
    "lagerbestand": 10
}

# Die Liste 'lager' erstellen
lager = [produkt_1, produkt_2, produkt_3]

# Initialisierung der Variablen
gesamter_warenwert = 0
einzel_preis = 50 # Angenommener Preis pro Stück

print("Lagerbestand")

# Verarbeitung Produkt 1
produkt = produkt_1
print(f"Produkt: {produkt['name']}, Aktueller Bestand: {produkt['lagerbestand']} Stück.")

# Gesamtwert für Produkt 1
wert_dieses_produkts = produkt["lagerbestand"] * einzel_preis
gesamter_warenwert = gesamter_warenwert + wert_dieses_produkts

# Verarbeitung Produkt 2
produkt = produkt_2
print(f"Produkt: {produkt['name']}, Aktueller Bestand: {produkt['lagerbestand']} Stück.")

# Gesamtwert für Produkt 2
wert_dieses_produkts = produkt["lagerbestand"] * einzel_preis
gesamter_warenwert = gesamter_warenwert + wert_dieses_produkts

# Verarbeitung Produkt 3
produkt = produkt_3
print(f"Produkt: {produkt['name']}, Aktueller Bestand: {produkt['lagerbestand']} Stück.")

# Gesamtwert für Produkt 3
wert_dieses_produkts = produkt["lagerbestand"] * einzel_preis
gesamter_warenwert = gesamter_warenwert + wert_dieses_produkts

print(" Zusammenfassung")
# Ausgabe des Gesamtwerts
print(f"Gesamter Warenwert des Lagers (bei {einzel_preis} €/Stück): {gesamter_warenwert:.2f} Euro")