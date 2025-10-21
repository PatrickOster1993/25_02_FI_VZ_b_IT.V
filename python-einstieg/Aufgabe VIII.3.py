# Variablen
faktor = 1       
ergebnis = 0     
basis_zahl = 2   

print(f"Multiplikationstabelle für die Zahl {basis_zahl}, bis das Ergebnis 50 erreicht oder überschreitet:")

# Die Schleife läuft, solange das Ergebnis NICHT größer als 50 ist (also <= 50).
while ergebnis <= 50:
    
    # 3. Das aktuelle Ergebnis berechnen
    ergebnis = basis_zahl * faktor
    
    
    # Berechnung außerhalb der Bedingung und dann prüfen:
    if ergebnis > 50:
        break

    # Das Ergebnis ausgeben
    print(f"{basis_zahl} x {faktor} = {ergebnis}")
    
    # Den Multiplikator erhöhen
    faktor += 1
   