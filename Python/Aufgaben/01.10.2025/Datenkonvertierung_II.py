#Aufgabe Währungsumrechner
#Variable Faktor 1€ ist 1.1$
faktor = 1.1
#Eingabe betrag==========
euro = float(input("Bitte Euro Betrag eingeben"))
#Berechnung==============
usd = euro*faktor
#Ausgabe================= 
print(f"{euro}€ entsprechen {usd:.2f}$")


#Aufgabe Temperaturkonvertierung 
#Eingabe Celsius=========
celsius = float(input("Bitte Temperatur in Celsius eingeben"))
#Berechnung==============
fahrenheit = (celsius*9/5)+32
#Ausgabe Fahrenheit======
print(f"{celsius}°C entspricht {fahrenheit:.2f}°F")


#Aufgabe Altersumrechnung
#Eingabe Alter in Jahren=
alter_jahre = int(input("Bitte Ihr Alter in ganzen Jahren eingeben"))
#Berechnung==============
alter_monate = alter_jahre*12
#Ausgabe des Alters in Monaten
print(f"Sie sind {alter_monate} Monate Jung ^^")
