einnahmen = [5000, 7000, 3000, 8000]
ausgaben = [4000, 6000, 2500, 6500]
gewinn_ueber_1000 = 0
monats_zaehler = 0 


print("\n--- Gewinnberechnung und Zähler ---")

# die Liste der Einnahmen
for einnahme in einnahmen:
    
    #  Wert der Ausgaben 
    ausgabe = ausgaben[monats_zaehler]
    
    gewinn = einnahme - ausgabe
    
    # Gewinn pro Monat ausgeben
    print(f"Monat {monats_zaehler + 1}: Einnahmen: {einnahme} € | Ausgaben: {ausgabe} € | Gewinn: {gewinn:.2f} €")
    
    # Zählen, wie viele Monate Gewinn > 1000 haben
    if gewinn > 1000:
        gewinn_ueber_1000 = gewinn_ueber_1000 + 1
        
    # für den nächsten Durchlauf erhöhen
    monats_zaehler = monats_zaehler + 1


print(f"\nMonate mit Gewinn > 1000 €: **{gewinn_ueber_1000}**")