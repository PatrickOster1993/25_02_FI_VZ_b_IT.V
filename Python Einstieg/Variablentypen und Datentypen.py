#                   2.Variabletypen und Datentypen
# Übung
#2.1 Datentypen identifizieren
#101 =Integer
#"False"=String
#False = Boolean
#3.141 = Float
#"-5" = String


# Übung 2.2: type() anwenden

# Variable mit Integer (ganze Zahl)
zahl = 42

# Variable mit Float (Kommazahl)
kommazahl = 3.14

# Variable mit String (Text)
text = "Hallo Welt"

# Variable mit Boolean (Wahrheitswert)
wahrheitswert = True

# Ausgabe der Datentypen
print("Der Datentyp von zahl ist:", type(zahl))
print("Der Datentyp von kommazahl ist:", type(kommazahl))
print("Der Datentyp von text ist:", type(text))
print("Der Datentyp von wahrheitswert ist:", type(wahrheitswert))



# Übung 2.3: Fehler provozieren

# Ein String (Text)
zahl_str = "10"

# Versuch, eine Zahl vom String zu subtrahieren == FEHLER
ergebnis = zahl_str - 5
print(ergebnis)
#TypeError: unsupported operand type(s) for -: 'str' and 'int'


# Übung 2.3: Fehler beheben

# Ein String (Text)
zahl_str = "10"

# String in Integer umwandeln
zahl_int = int(zahl_str)

# Jetzt funktioniert die Subtraktion
ergebnis = zahl_int - 5
print("Das Ergebnis lautet:", ergebnis)
# Ausgabe: Das Ergebnis lautet: 5



# Übung 2.3: Zweite korrigierte Version (int -> str)

zahl_str = "10"
zahl_int = 5

# Zahl in String umwandeln
zahl_text = str(zahl_int)

# Jetzt Strings verketten
ergebnis = zahl_str + " - " + zahl_text
print("Die Ausgabe lautet:", ergebnis)
#Die Ausgabe lautet: 10 - 5
