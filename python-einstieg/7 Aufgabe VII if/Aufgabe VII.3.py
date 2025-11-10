# DATENDEFINITON 

Zimmerpreis_pP = 80.00          # Preis pro Person und Nacht (Beispielwert)
Aufenthaltsdauer = 3            # Beispiel: 3 Nächte
AnzahlErwachsene = 2            # Festgelegt: Zwei Erwachsene

# Rabattsätze
Rabatt_Gratis = 100
Rabatt_Senior = 70


#  BENUTZEREINGABE 

print("--- FAMILIENANGEBOT RECHNER ---")

# Abfragen des Alters des Kindes und Umwandlung in eine ganze Zahl
EingabeAlterKind_str = input("Bitte geben Sie das Alter des Kindes ein: ")
AlterKind = int(EingabeAlterKind_str)


# BERECHNUNG DER RABATTSTUFE

# Rabatt initialisieren
Rabatt = 0

# Wenn Alter des Kindes kleiner 7, dann Rabatt = 100%
if AlterKind < 7:
    Rabatt = Rabatt_Gratis # 100
else:
    # Sonst (Alter >= 7 Jahre) Rabatt = 70%
    Rabatt = Rabatt_Senior # 70

print(f"Das Kind ist {AlterKind} Jahre alt. Es gilt ein Rabatt von {Rabatt} %.")


# PREISBERECHNUNGEN

# Preis für die Erwachsenen (Voller Preis)
PreisErwachsene = Zimmerpreis_pP * Aufenthaltsdauer * AnzahlErwachsene

# Preis für das Kind (Mit Rabatt)
zu_zahlender_Anteil = 1 - (Rabatt / 100)
Kinderpreis = Zimmerpreis_pP * Aufenthaltsdauer * zu_zahlender_Anteil


# Gesamtpreis
Gesamtpreis = PreisErwachsene + Kinderpreis


# AUSGABE

print("\n--- ANGEBOT (Netto) ---")
print(f"Erwachsenenpreis ({AnzahlErwachsene} Personen): {PreisErwachsene:.2f} Euro")
print(f"Kinderpreis ({AlterKind} Jahre, {Rabatt}% Rabatt): {Kinderpreis:.2f} Euro")
print(f"Gesamtpreis für die Familie: {Gesamtpreis:.2f} Euro")