#aufgabe 1

Anzahl_der_Personen=int(input("wie veile der personen :  "))
Aufenthaltsdauer=int(input("Geben Sie Aufenthaltsdauer ein :   "))


Zimmerpreis_für_person = int(70)
Mehrwertsteuer =float(1.19)
Mehrwertsteuer2=float(0.19)
 
Nettopreis =(Zimmerpreis_für_person*Aufenthaltsdauer*Anzahl_der_Personen)
Gesamtpreis = (Nettopreis *Mehrwertsteuer)
Mehrwertsteuer1=(Gesamtpreis*Mehrwertsteuer2)

print(f"Nettoüreis : {Nettopreis} €")
print (f"Gesamtpreis mit steuer : {Gesamtpreis:.2f} €")
print (f"Netto = {Nettopreis} € und Steue {Mehrwertsteuer1:.2f} €")

#aufgabe2 

#die Menge verschiedenen Lebensmitteln
anzahl_apfel=int(5)
anzahl_banannen=int(10)
anzahl_orange=int(8)

# die Preis von verschiedenen Lebensmitteln
preis_apfel=float(1.5)
preis_banannen=float(2.5)
preis_orange=float(3.5)

#Gesamt preis der jeder 
Gesamtpreis_apfle=(anzahl_apfel*preis_apfel)
Gesamtpreis_banannen=(anzahl_banannen*preis_banannen)
Gesamtpreis_orange=(anzahl_orange*preis_orange)

#Gesamt preis Addiern 
Gesamtpreis=(Gesamtpreis_apfle+Gesamtpreis_banannen+Gesamtpreis_orange)



print(f"Gesamt preis lebensmitteln ist :{Gesamtpreis: .2f} €")

