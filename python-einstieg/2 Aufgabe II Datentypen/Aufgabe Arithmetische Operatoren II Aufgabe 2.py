# 1. Definierte Werte (Ihre Angaben)
netto_betrag = 120.00
steuer_betrag = 7.00

# 2. Berechnung
brutto_betrag = netto_betrag + steuer_betrag

# 3. Konsolenausgabe
print("--- Bruttobetrag Berechnung ---")

# Zahlenwerte mithilfe von str() in Text umgewandeln
print("Nettobetrag: " + str(netto_betrag) + " Euro")
print("Steuerbetrag: " + str(steuer_betrag) + " Euro")
print("------------------------------")
print("Bruttobetrag: " + str(brutto_betrag) + " Euro")