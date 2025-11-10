# Speicherung der Menge als int
menge_aepfel = 8
menge_bananen = 5
menge_orangen = 12

# Speicherung der Preise pro Stück als float
preis_pro_apfel = 0.59
preis_pro_banane = 0.35
preis_pro_orange = 0.79

# 2. Berechnung der Gesamtpreise pro Obstart

# Gesamtpreis Äpfel = Menge * Preis
gesamt_aepfel = menge_aepfel * preis_pro_apfel

# Gesamtpreis Bananen = Menge * Preis
gesamt_bananen = menge_bananen * preis_pro_banane

# Gesamtpreis Orangen = Menge * Preis
gesamt_orangen = menge_orangen * preis_pro_orange

# 3. Berechnung des Gesamteinkaufs

# Gesamtbetrag = Summe aller Einzelpreise
gesamt_einkauf = gesamt_aepfel + gesamt_bananen + gesamt_orangen

# Konsolenausgabe

print("--- Einkauf Gesamtübersicht ---")
print("Apfelpreis (Gesamt): " + str(gesamt_aepfel) + " €")
print("Bananenpreis (Gesamt): " + str(gesamt_bananen) + " €")
print("Orangenpreis (Gesamt): " + str(gesamt_orangen) + " €")
print("---------------------------------")
print("Gesamtbetrag des Einkaufs: " + str(gesamt_einkauf) + " €")
print("---------------------------------")