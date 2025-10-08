print("Wieviel Geld möchten Sie abheben")
eingabe=input()#Benuzereingabe

if eingabe.isdigit():#prüfe ob die Eingabe eine gültige Zahl ist
    kapital=int(eingabe)
    if kapital <=100:
        print("Sie können maximal bis 100 Euro abheben")
    elif kapital<=150:
        print("Sie können maximal zwichen 101 und150")
    elif kapital==200:
        print("Sie können auch direkt 200 Euro abheben")
    else:#alles andere
        print("Soviel Geld haben Sie nicht")
else:   
    print("Sonst hast du keine anderen Probleme oder?!")
    