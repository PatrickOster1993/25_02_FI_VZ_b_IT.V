# Konstante für die Mehrwertsteuer (19%)
MWST_SATZ = 0.19

# Benutzereingaben abfragen
produkt = input("Maus")
nettopreis= input(195.99)
stueckzahl = input(2)

# Typumwandlung: String → float / int
nettopreis = float(195.99)
stueckzahl = int(2)

# Berechnungen
gesamt_netto = nettopreis * stueckzahl
mwst_betrag = gesamt_netto * MWST_SATZ
gesamt_brutto = gesamt_netto + mwst_betrag

# Ausgabe formatieren (numerische Werte in Strings umwandeln)
print("\n--- Bestellzusammenfassung ---")
print("Maus: " + produkt)
print("Gesamt-Nettopreis: " + str(gesamt_netto) + " EUR")
print("+ 19% MwSt.: " + str(mwst_betrag) + " EUR")
print("Gesamt-Bruttopreis: " + str(gesamt_brutto) + " EUR")