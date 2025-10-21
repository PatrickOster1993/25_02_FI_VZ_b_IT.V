# Festgelegte Konstanten (Zimmerpreis und Mehrwertsteuersatz)
Zimmerpreis = 70.00
Mwst_Satz = 0.19 # 19% als Dezimalwert
Mwst_Faktor = 1 + Mwst_Satz # Multiplikator 1.19
Aufschlag_Einzelnacht = 20.00


# BENUTZEREINGABE

print("--- HOTELBUCHUNGS-RECHNER ---")

# Abfragen der Benutzerdaten und Umwandlung in ganze Zahlen
# 
EingabeAufenthaltsdauer_str = input("Aufenthaltsdauer in Tagen: ")
EingabeAnzahlDerPerson_str = input("Anzahl der Personen: ")

# Umwandlung der Eingaben in Zahlen
Aufenthaltsdauer = int(EingabeAufenthaltsdauer_str)
AnzahlDerPersonen = int(EingabeAnzahlDerPerson_str)


# BERECHNUNG DES NETTOBETRAGS

Nettopreis = Zimmerpreis * Aufenthaltsdauer * AnzahlDerPersonen


#  AUFSCHLAGSPRÜFUNG

if Aufenthaltsdauer == 1:
    print(f"\nEs wird ein Aufschlag von {Aufschlag_Einzelnacht:.2f} Euro für die Einzelnacht berechnet.")
    # Füge den Aufschlag zum Nettobetrag hinzu
    Nettopreis = Nettopreis + Aufschlag_Einzelnacht


#  BERECHNUNG DES GESAMTPREISES

Gesamtpreis = Nettopreis * Mwst_Faktor
Mwst_Betrag = Gesamtpreis - Nettopreis # Optional, für die Ausgabe schöner

print("\n--- ERGEBNISSE ---")
print(f"Nettobetrag (inkl. Aufschlag): {Nettopreis:.2f} Euro")
print(f"Mehrwertsteuer (19%): {Mwst_Betrag:.2f} Euro")
print(f"Gesamtpreis (Brutto): {Gesamtpreis:.2f} Euro")