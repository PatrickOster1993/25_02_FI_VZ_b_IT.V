umsatz = [1200, 1500, 900, 2000, 1700, 1300]
gesamtumsatz = 0
anzahl_monate = 0 

# Gesamtumsatz und Anzahl der Monate berechnen
for monatsumsatz in umsatz:
    gesamtumsatz = gesamtumsatz + monatsumsatz
    anzahl_monate = anzahl_monate + 1

# Durchschnitt berechnen
durchschnitt = gesamtumsatz / anzahl_monate

print("--- Umsatzanalyse ---")
print(f"Gesamtumsatz: {gesamtumsatz:.2f} €")
print(f"Durchschnittlicher Monatsumsatz: {durchschnitt:.2f} €")
print("\nUmsätze ÜBER dem Durchschnitt:")

# Überdurchschnittliche Umsätze ausgeben
for monatsumsatz in umsatz:
    if monatsumsatz > durchschnitt:
        print(f"  > {monatsumsatz:.2f} €")