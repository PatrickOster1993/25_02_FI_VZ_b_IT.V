print("Wieviel Geld möchten Sie abheben? ")
eingabe = input()

if eingabe.isdigit():
    kapital = int(eingabe)

    if kapital <100 and kapital >0: 
        print("Sie können maximal bis 99€ abheben, Ihre Eingabe wird verarbeitet.")
    else: print("Einfach nein")