print("")
print("Preisrechner:")
print("")

produkt=input("Bitte geben sie den Namen des Produkts ein: ")
netto=input("Bitte geben sie den Nettopreis ein: ")
zahl=input("Bitte geben sie die Stückzahl ein: ")

#Berechnung von Gesamt-Nettopreis, Mehrwertsteuer und Gesamt-Bruttopreis
GNetto=(float(netto)*int(zahl))
MwSt=(GNetto*0.19)
Brutto=(GNetto+MwSt)

print("")
print("========Bestellzusammenfassung========")
print("")
print("           Produkt: ",produkt)
print(" Gesamt-Nettopreis: ",GNetto,"Euro")
print("        +19% MwSt.: ",round(MwSt, 2),"Euro")
print("Gesamt-Bruttopreis: ",round(Brutto, 2),"Euro")
print("")