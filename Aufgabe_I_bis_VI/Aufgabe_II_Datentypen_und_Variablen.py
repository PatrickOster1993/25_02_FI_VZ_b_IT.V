#Aufgabe 1: Deklaration mehrerer Variablen
#Deklariere drei Variablen, um die Namen, das Alter und die Höhe (in Metern) von zwei verschiedenen Personen zu speichern. 
#Initialisiere die Variablen mit beliebigen Werten.

#nebeneinander
variable1name, variable1alter, variable1höhe = "Anna", 24, 1.78

#untereinander
variable1name=      "Anna"
variable1alter=     24
variable1höhe=      1.78

person2name=        "David"
person2alter=       36
person2höhe=        1.92

#Ausgabe
print (f"{variable1name} ist {variable1alter} alt und ist {variable1höhe} groß")
print (f"{person2name} ist {person2alter} alt und ist {person2höhe} groß")




#Aufgabe 2: Berechnung und Zuweisung
#Deklariere zwei Variablen vom Typ float, um die Länge und Breite eines Rechtsecks zu bestimmen.
#Berechne die Fläche und speichere das Ergebnis in einer dritten Variable

länge= 3.1      #Bsp. für die Länge
breite= 6.7     #Bsp. für die Breite

#Fläche berechnen
Fläche= länge * breite

#Ausgabe
print ("Die Fläche des Rechtecks beträgt:", Fläche)




#Aufgabe 3: Deklariere und Intialisiere
#Deklariere und initialisiere folgende Variablen:
#Einen int-Wert für das Alter einer Person.
#Einen float-Wert für die Temperatur.
#Einen string-Wert für den Namen eines Haustiers.
#Einen bool-Wert, der angibt, ob es draußen regnet nur wenn ihr es könnt

Alter=          25
Temperatur=     18.5
Haustier=       "Herbert"
es_regnet=      False

#Ausgabe
print ("Alter", Alter)
print ("Temperatur:", Temperatur)
print ("Haustier", Haustier)
print ("regnet es draußen?", es_regnet)	
print (f"Hallo ich heiße Max, ich bin {Alter} Jahre alt und gehe mit meinem Hund {Haustier} bei {Temperatur} grad draußen spazieren")




#Aufgabe 4: Deklariere und Initialisiere
#Deklariere und initialisiere Variablen, um folgendes zu berechnen:
#Das Ergebnis einer Addition von zwei int-Zahlen
#Die Fläche eines Kreises mit einem gegebenen Radius (benutze float für die Berechnungen)
#Eine Nachricht, die zwei Strings miteinander kombiniert

#Addition von zwei int. Zahlen

zahl1=          6
zahl2=          13
addition_ergebnis= zahl1 + zahl2
print (addition_ergebnis)

#Fläche eines Kreises - float
Radius= 7.3
Kreisfläche= 3.14159 * Radius
print (Kreisfläche)

#zwei Strings miteinander kombinieren
Name_eins= "Max Mustermann"
Name_zwei= "Johanna Joppie"
print (f"{Name_eins} & {Name_zwei}")




#Aufgabe 5:
#Erstelle ein Programm, das den Namen, das Alter und das Lieblingsessen eines Nutzers speichert.
#Gib diese Informationen in einem Satz aus, z. B.: „Hallo Max, du bist 25 Jahre alt und dein
#Lieblingsessen ist Pizza.

Name=               "Max Mustermann"
Alter=              25
Lieblingsessen=     "Pizza"

#Ausgabe
print(f"Hallo {Name}, du bist {Alter} Jahr alt und dein Lieblingsessen ist {Lieblingsessen}.")




