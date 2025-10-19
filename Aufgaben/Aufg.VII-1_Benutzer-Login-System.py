#Benutzer-Login-System

print("\nRegistrierung: ")

zaehler = 0

benutzername_reg = input("\nBitte erstellen sie einen neuen Benutzernamen: ")
passwort_reg = input("\nBitte erstellen sie ein neues Passwort: ")

benutzername = input("\nBitte geben sie ihren Benutzernamen ein: ")

while benutzername_reg != benutzername:
    print("\nLeider Falsch")
    benutzername = input("\nBitte geben sie ihren Benutzernamen ein: ")
    zaehler = zaehler+1
    if zaehler == 3:
        print("\nZu viele falsche Versuche versuchen sie es später noch einmal!")
        print("")
        quit()
print("Korrekt!")

passwort = input("\nBitte geben sie ihr Passwort ein: ")

while passwort_reg != passwort:
    print("\nLeider Falsch")
    passwort = input("\nBitte geben sie ihr Passwort ein: ")
    zaehler = zaehler+1
    if zaehler == 3:
        print("\nZu viele falsche Versuche versuchen sie es später noch einmal!")
        print("")
        quit()
print("Korrekt!")

print("\nSie sind nun eingelogt")
print("")
