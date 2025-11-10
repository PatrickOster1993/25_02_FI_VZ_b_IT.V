# Variablen 
zahl = 1      
summe = 0      

print("Berechnung der Summe der ersten 5 positiven ganzen Zahlen (1 + 2 + 3 + 4 + 5):")

# Die Schleife läuft, solange 'zahl' kleiner oder gleich 5 ist.
while zahl <= 5:
    
    # Addieren der aktuellen Zahl zur Summe
    summe = summe + zahl
    
    # Zahl erhöhen
    zahl = zahl + 1

# Finale Ausgabe des Ergebnisses
print(f"Die berechnete Summe beträgt: {summe}")