# # Konstanten
ZIMMERPREIS_NETTO = 70.0  # Euro pro Person und Nacht
MEHRWERTSTEUER = 0.07     # 7% für Hotelübernachtungen (0.07)

# 1. Eingabe von Daten
print("Angebot für Hotelübernachtungen")

# Eingabe der Anzahl der Personen
anzahl_personen_str = input("Anzahl der Personen: ")

# Eingabe der Aufenthaltsdauer
aufenthaltsdauer_str = input("Aufenthaltsdauer (Nächte): ")

# 2. Datenkonvertierung (von String zu Integer/Float)
anzahl_personen = int(anzahl_personen_str)
aufenthaltsdauer = int(aufenthaltsdauer_str)

# 3. Berechnung des Gesamtpreises

# Nettopreis = Zimmerpreis x Aufenthaltsdauer x Anzahl der Personen
nettopreis = ZIMMERPREIS_NETTO * aufenthaltsdauer * anzahl_personen

# Mehrwertsteuer (Betrag)
mwst_betrag = nettopreis * MEHRWERTSTEUER

# Gesamtpreis (Bruttopreis) = Nettopreis + Mehrwertsteuer
gesamtpreis = nettopreis + mwst_betrag

# 4. Ausgabe des Gesamtpreises
print("\n--- Ergebnis ---")
print(f"Nettopreis (ohne MWSt): {nettopreis:.2f} €")
print(f"Mehrwertsteuer (7%): {mwst_betrag:.2f} €")
print(f"--------------------------------------")
print(f"Gesamtpreis (Brutto): {gesamtpreis:.2f} €")
print("--------------------------------------")