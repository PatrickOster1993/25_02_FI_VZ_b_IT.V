#aufgabe 1 Euro in DOLLAR

#wechselkurs 
wechselkurs=float(1.1)
#Eingabe Euro 
eingabe=float(input("Geben Sie die preise in Euro : "))
aktuellerwechselkurz=float(input("betrag in Euro , sofern Sie Geld habe : "))
#umrechnung 
ausgabe= (eingabe*aktuellerwechselkurz)
#Ausgabe
print(f"die preis in Dollar : {ausgabe:.2f} $")

# ---------------------------------------------------------------------------------------
#aufgabe 2 
#Eingabe Temparatur
celsius = float(input("Gib die Temperatur in Celsius ein: "))
# Umrechnung
fahrenheit=(celsius*9/5)+32
# Ausgabe
print(f"{celsius:.2f} C entsprechen {fahrenheit:.2f} F.")

#------------------------------------------------------------------------------------------
#aufgabe3

#eingabe
eingabe_alt=int(input("wie Alt sind Sie :"  ))
#umrechnung 
Monaten=(12)
Alter=(eingabe_alt*Monaten)
#Ausgabe
Alter=print(f"Dein Alter in Monaten beträgt: {Alter} Monaten")





