ist_registriert = True
nutzer=input("Trage bitte deinen Benutzernamen ein")

if ist_registriert:#true ausgeführt siehe oben
    print("Du bist Registriert")
    if nutzer != "":

        print(f"Hi {nutzer}")
        if nutzer == "Herr Cakir":
            print("Guten Morgen lieber Herr Cakir, schön das sie da sind")
else:
    print("Sie sind nicht Registriert")


## wie sieht es aus wenn ich eine falscheingabe mache oder die Person bzw Benutzernamen vergeben sind
