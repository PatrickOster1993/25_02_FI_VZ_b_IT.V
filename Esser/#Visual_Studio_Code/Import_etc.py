
#Import einer Funktion - Verwendun zu einer "Glücksspiel"

import random

eingabe = input("Geben Sie eine Ganzzahl an ")

if eingabe.isdigit():
    eingabe = int(eingabe)
    random_number = random.randint(1,10)
    randomnachkomma = random.randint(1,9)
    randomvalue = float(randomnachkomma)/10
    Ergebnis = random_number+randomvalue
    print(Ergebnis)

    if eingabe==random_number: 
        print("Sie haben gewonnen!")
    else:
     print(f"Leider verloren, die richtige Zahl war {random_number}  ")

# Weitere Random-Funktion:

print(int(random.uniform(1, 77)))

#Registrierung
print("Bitte trage zunächst deinen Benutzernamen fü die Registrierung ein:  ")
username = input()

print("Bitte tragen Sie ein Passwort ein:   ")
password = input()

#Login
print("gebe bitte jetzt deinen Nutzernamen ein: ")
input_username = input()
if input_username==username:
    print("Richtige Eingabe des Benutzernamens")
    print("Geben Sie jetzt ihr Paswort ein")
    input_password = input()

    if input_password==password:
        print ("Einloggen erfolgreich")
    else:
        print("Login falsch")
else: 
    print("Falscher Benutzername")