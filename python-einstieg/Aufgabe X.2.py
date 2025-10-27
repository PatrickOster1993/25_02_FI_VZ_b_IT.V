#  Benutzereingabe abfragen
eingabe_str = input("Geben Sie die Zahl ein, deren Multiplikationstabelle Sie sehen möchten: ")
basis_zahl = int(eingabe_str)

print(f"\nMultiplikationstabelle für die Zahl {basis_zahl} (bis 10):")

#  Die for-Schleife
for faktor in range(1, 11):
    ergebnis = basis_zahl * faktor
    
    #  Das Ergebnis ausgeben
    print(f"{basis_zahl} x {faktor} = {ergebnis}")