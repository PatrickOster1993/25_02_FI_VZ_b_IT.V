#Aufgabe Preisrechner
name=input("Name des Produkts eingeben")
nettopreis=float(input("Nettopreis eingeben"))
menge=int(input("Stückzahl eingeben"))
mwst=0.19

gnetto=nettopreis*menge
Amwst=gnetto*mwst
gesamt=gnetto+Amwst

str(gnetto)
str(Amwst)
str(gesamt)

print("===Ihre zusammenfassung===")
print(f"Produkt:             {name}")
print(f"Gesamt-Nettopreis:   {gnetto} EUR")
print(f"+ 19% MwSt.:         {Amwst} EUR")
print(f"Gesamt-Bruttopreis:  {gesamt} EUR")
