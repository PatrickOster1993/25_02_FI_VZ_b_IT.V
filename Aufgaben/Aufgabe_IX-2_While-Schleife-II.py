# Einfache Passwortprüfung 

passwort = "12345"

zaehler = 1

pass_eingabe = input("Bitte geben sie ihr Passwort ein: ")

while pass_eingabe != passwort:
    print("\nLeider Falsch")
    pass_eingabe = input("\nBitte geben sie ihr Passwort ein: ")
    zaehler+= 1
    if zaehler == 3 and pass_eingabe != passwort:
        print("\nZu viele falsche Versuche versuchen sie es später noch einmal!")
        print("")
        quit()
print("\nKorrekt!")
print("")
