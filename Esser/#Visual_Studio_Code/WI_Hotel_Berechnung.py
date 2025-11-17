ist_registriert = True# Dieser boolsche Wert MUSS NICHT gesetzt werden - Siehe Zeile 4
nutzer = input("Trage bitte deinen Benutzernamen ein ")

if ist_registriert: # Hier kann auch ein NICHT-Verknüpfter Wert stehen also z.b. OHNE Zeile 1 und dann: 1==1 für True oder 1==2 für False ( Führe aus oder Führe nicht aus )
    print("Du bist registriert")
    if nutzer != "": #Keine LEERE Eingabe
        print(f"Hi {nutzer}")
        if nutzer == "Herr Cakir":
            print(" Guten Morgen lieber Herr Cakir, schön dass Sie da sind")
else:
    print("Sie sind nicht registriert")
