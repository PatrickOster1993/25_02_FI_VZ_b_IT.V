

print("--- 1. REGISTRIERUNG ---")

#  Eingaben für die Registrierung abfragen
gespeicherter_benutzername = input("Wählen Sie einen Benutzernamen: ")
gespeichertes_passwort = input("Wählen Sie ein Passwort: ")

print("Registrierung erfolgreich! Ihre Daten wurden gespeichert.")
print("-" * 35)


#  LOGIN-PRÜFUNG

print("--- 2. LOGIN ---")

# Login-Eingaben abfragen
eingegebener_benutzername = input("Benutzername: ")
eingegebenes_passwort = input("Passwort: ")

# Überprüfung mit if-else

# Prüfe, ob der eingegebene Benutzername mit dem gespeicherten übereinstimmt
if eingegebener_benutzername == gespeicherter_benutzername:
    
    # Nun das Passwort prüfen.
    if eingegebenes_passwort == gespeichertes_passwort:
        
        # Login erfolgreich
        print("\n WILLKOMMEN! Der Login war erfolgreich.")
    
    else:
        # Passwort falsch (Benutzername war richtig)
        print("\n Login fehlgeschlagen: Das Passwort ist falsch.")
        
else:
    # Benutzername existiert nicht (stimmt nicht mit dem gespeicherten Namen überein)
    print("\n Login fehlgeschlagen: Der Benutzername existiert nicht.")

print("-" * 35)
print("Programmende.")