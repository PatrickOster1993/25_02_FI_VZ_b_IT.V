#  Benutzereingabe abfragen
eingabe_str = input("Geben Sie die Zahl (N) ein, bis zu der die Quadratzahlen summiert werden sollen: ")
grenze_n = int(eingabe_str)

#  Variablen für die Summierung
summe_quadratzahlen = 0

print(f"\nBerechne Summe der Quadratzahlen von 1 bis {grenze_n}:")

#  Die for-Schleife
for zahl in range(1, grenze_n + 1):
    
    #  Quadratzahl berechnen
    quadrat = zahl * zahl
    
    #  Quadratzahl zur Gesamtsumme hinzufügen
    summe_quadratzahlen = summe_quadratzahlen + quadrat
    
    
#  Endgültige Summe ausgeben
print(f"\nDie finale Summe der Quadratzahlen beträgt: {summe_quadratzahlen}")