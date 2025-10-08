print("Wieviel Geld möchten sie abheben?")

eingabe=input()#Benutzereingabe

if eingabe.isdigit():#prüft ob die Eingabe eine Zahl ist. Wenn ich tatsächlich zahl integer eingegeben habe dann gehe einen Schritt weiter
    Kapital=int(eingabe)

    if Kapital <100:
        print("Sie können maximal bis 100 Euro abheben")
    elif Kapital >=100 and Kapital<=150:
        print("Sie können maximal zwischen 101 und 150 Euro abheben")
    elif Kapital ==200:
        print("Sie können auch direkt 200 Euro abheben")
    else:#alles andere
        print("Soviel Geld haben sie nicht")
else:
    print("Sonst hast du keine andere Probleme oder?")

    