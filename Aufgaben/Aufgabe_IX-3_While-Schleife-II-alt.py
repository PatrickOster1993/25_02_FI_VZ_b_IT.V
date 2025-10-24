# Anzahl der Ziffern einer Zahl zählen

zahl = input("\nBitte geben sie eine positive ganze Zahl ein: ")

zaehler = 1

try:
    zahl = int(zahl)
except ValueError:
    print("\nSie müssen eine ganze Zahl eingeben!")
    print("")
    quit()

if zahl >= 0:    
    while zahl > 9:
        zahl = zahl/10
        zaehler+=1
else:
    print("\nSie müssen eine positive Zahl eingeben!")
    print("")
    quit()

print(f"\nDiese Zahl hat {zaehler} Ziffern")
print("")
