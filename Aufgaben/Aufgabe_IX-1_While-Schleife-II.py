# Benutzer gibt positive Zahlen ein und berechnet den Durchschnitt 

eingabe_zahl = float(input("\nBitte geben sie eine positive Zahl ein: "))

x = []

while eingabe_zahl >= 0:
    x.append(eingabe_zahl)
    durchschnitt = sum(x)/len(x)
    print(f"\nDer Durchschnitt der Zahlen beträgt {durchschnitt:.2f}")
    eingabe_zahl = float(input("\nBitte geben sie eine weitere positive Zahl ein: "))
print("\nDas war keine positive Zahl!")
print("")
