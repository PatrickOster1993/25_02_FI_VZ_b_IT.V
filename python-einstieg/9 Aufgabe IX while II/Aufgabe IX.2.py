# Konstanten
KORREKTES_PASSWORT = "passwort123"
MAX_VERSUCHE = 3

# Zähler
versuche_gemacht = 0

print("--- PASSWORTEINGABE ---")
print(f"Sie haben maximal {MAX_VERSUCHE} Versuche.")

# 3. while-Schleife: Läuft, solange die Versuche unter dem Limit liegen
while versuche_gemacht < MAX_VERSUCHE:

    # Zähler erhöhen
    versuche_gemacht = versuche_gemacht + 1

    # Eingabe des Benutzers anfordern
    eingegebenes_passwort = input(f"Versuch {versuche_gemacht}/{MAX_VERSUCHE}: Geben Sie das Passwort ein: ")

    # Prüfung mit if/else
    if eingegebenes_passwort == KORREKTES_PASSWORT:
        print("\n Zugang gewährt! Das Passwort ist korrekt.")
        break 
    else:
        # Falsche Eingabe
        if versuche_gemacht < MAX_VERSUCHE:
            print("Falsches Passwort. Bitte versuchen Sie es erneut.")

# Abschließende Prüfung
# Wenn die Schleife nicht durch 'break' beendet wurde
if versuche_gemacht == MAX_VERSUCHE and eingegebenes_passwort != KORREKTES_PASSWORT:
    print("\n Zu viele Fehlversuche. Der Zugang wurde gesperrt.")