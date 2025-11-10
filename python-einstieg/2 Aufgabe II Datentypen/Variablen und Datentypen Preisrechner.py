# Definition der Mehrwertsteuer
MWST_SATZ = 0.19

# Abfrage der Benutzerinformationen
produkt_name = input("Geben Sie den Namen des Produkts ein: ")
netto_preis_str = input("Geben Sie den Nettopreis des Produkts in EUR ein (z.B. 79.99): ")
stueckzahl_str = input("Geben Sie die gewünschte Stückzahl ein (z.B. 2): ")

# Typumwandlung (Type Casting) der Benutzereingaben
# Umwandlung des Preises in einen float für Berechnungen
netto_preis = float(netto_preis_str)
# Umwandlung der Stückzahl in einen int
stueckzahl = int(stueckzahl_str)

# Berechnung der Kosten
# Gesamter Nettopreis (Netto pro Stück * Stückzahl)
gesamt_netto_preis = netto_preis * stueckzahl

# Mehrwertsteuer (Gesamt-Nettopreis * Mehrwertsteuersatz)
mehrwertsteuer = gesamt_netto_preis * MWST_SATZ

# Gesamtbruttopreis (Gesamt-Nettopreis + Mehrwertsteuer)
gesamt_brutto_preis = gesamt_netto_preis + mehrwertsteuer

# Formatierte Ausgabe der Ergebnisse
print("\n--- Bestellzusammenfassung ---")
print("Produkt: " + produkt_name)
# Umwandlung der numerischen Ergebnisse in Strings für die Ausgabe
print("Gesamt-Nettopreis: " + str(round(gesamt_netto_preis, 2)) + " EUR")
print("+ 19% MwSt.: " + str(round(mehrwertsteuer, 2)) + " EUR")
print("Gesamt-Bruttopreis: " + str(round(gesamt_brutto_preis, 2)) + " EUR")