#Aufgabe 1 Benutzer Login
benutzer_1 = {}
print("Willkommen bei der Registrierung\nBitte geben sie einen Benutzernamen ein.")
benutzer_1["name"] = input()
print("Bitte geben sie ein Password ein")
benutzer_1["password"] = input()

print("Bitte melden Sie sich an")
while True:
    print("Bitte Benutzernamen eingeben")
    name = input()
    print(name)
    if name == benutzer_1["name"]:
        print(f"Hallo {name} bitte geben Sie ihr Password ein")
        password = input()
        if password == benutzer_1["password"]:
            print("Sie haben sich erfolgreich Angemeldet")
            break
        else:
             print("Benutzername und Password stimmen nicht überein")
    else:
        print("Benutzername existiert nicht")
