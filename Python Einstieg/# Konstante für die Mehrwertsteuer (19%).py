# Konstante für die Mehrwertsteuer (19%)
MWST_SATZ = 0.19

# Benutzereingaben abfragen
produkt_name = input("Maus: ")
nettopreis_str = float(input (229.99))
stueckzahl_str = int(input(50))

# Typumwandlung
nettopreis = float(nettopreis_str)
stueckzahl = int(stueckzahl_str)

# Berechnungen
gesamt_netto = nettopreis * stueckzahl
mwst_betrag = gesamt_netto * MWST_SATZ
gesamt_brutto = gesamt_netto + mwst_betrag

# Ausgabe mit str() wie gefordert
print("\n--- Bestellzusammenfassung ---")
print("Produkt: " + produkt_name)
print("Gesamt-Nettopreis: " + str(gesamt_netto) + " EUR")
print("+ 19% MwSt.: " + str(mwst_betrag) + " EUR")
print("Gesamt-Bruttopreis: " + str(gesamt_brutto) + " EUR")
