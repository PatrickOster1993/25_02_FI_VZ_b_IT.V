print("Hallo bitte Registrieren sie sich")
Benutzernamen=input()
print("Bitte vergeben sie ein Passwort")
Passwort=input(f"Hallo {Benutzernamen} bitte gebe dein passwort ein")
print("Registrierung erfolgreich, sie können sich einloggen")

print("Loggen sie sich bitte ein")
benutzernamen=input("Geben sie hier ihren Benutzernamen ein")
passwort=input("Bitte geben sie hier ihr Passwort ein")

if benutzernamen==Benutzernamen and passwort==Passwort:
    print(f"{benutzernamen} haben sich erfolgreich angemeldet")
else:
    print("Sie haben Flasche Daten eingegeben")
