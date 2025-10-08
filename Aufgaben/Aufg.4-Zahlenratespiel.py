# Zahlenratespiel

import random

random_number = random.randint(1,100)
eingabe = 0
zaehler = 0

print("")

while eingabe != random_number:
    zaehler = zaehler+1
    eingabe = input("Bitte Geben Sie eine eine ganze Zahl zwischen 1 und 100 ein: ")
    if eingabe.isdigit():
        eingabe = int(eingabe)
        if eingabe > random_number:
            print("Ihre Zahl ist zu hoch, veruschen sie es erneut")
            print("")
        elif eingabe < random_number:
            print("Ihre Zahl ist zu niedrig, versuchen sie es erneut")
            print("")
        else:
            print(f"Richtig geraten! Sie haben gewonnen! Die gesuchte Zahl war: {random_number}")
            print(f"sie haben insgesamt {zaehler} versuche gebraucht")
            print("")
    else:
        print("Das war keine gültige Zahl, starten sie das Spiel neu!")
        print("")     
        quit()
