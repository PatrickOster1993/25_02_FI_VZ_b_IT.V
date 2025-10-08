# Umrechnungskurs
UMRECHNUNGSKURS = 1.1  # 1 Euro = 1.1 US-Dollar

# 1. Eingabe des Betrags in Euro
print("--- Euro in US-Dollar Umrechner ---")


euro_betrag_str = input("Geben Sie den Betrag in Euro (€) ein: ")
euro_betrag = float(euro_betrag_str)

# 2. Berechnung des Betrags in US-Dollar
dollar_betrag = euro_betrag * UMRECHNUNGSKURS

# 3. Ausgabe des Ergebnisses
print("\n--- Ergebnis ---")

# Konvertierung der Float-Werte in String (Text)
print("Der Betrag von " + str(euro_betrag) + " € entspricht:")
print("US-Dollar: " + str(dollar_betrag) + " $")
print("----------------")