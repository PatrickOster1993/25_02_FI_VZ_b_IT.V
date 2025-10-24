# Berechne die Summe der Quadratzahlen 

zahl = int(input("Bitte geben sie eine positive ganze Zahl ein: "))

ergebniss = 0

for i in range(1,zahl+1):
    ergebniss+= i*i 
print(ergebniss)
