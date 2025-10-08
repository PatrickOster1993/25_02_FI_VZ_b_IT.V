a = 50
if a < 40:
    print("Die Zahl ist kleiner 40")


n = 50
if n < 40:
    print("Die Zahl ist kleiner als 40")
else:
    print("Die Zahl ist größer als 40")


b = 60
if b < 40:
    print("die Zahl ist kleiner als 40")
elif b > 40:
    print("Die Zahl ist größer als 40")
else:
    print("Die Zahl ist gleich 40")


eingabe = input("Wie viel Geld wollen Sie abheben?")

if eingabe.isdigit():
    kapital = int(eingabe)

    if kapital <= 100:
        print("Sie können maximal bis 100 Euro abheben")
    elif kapital >= 101 and kapital <= 150:
        print("Sie können maximal zwischen 101 und 150")
    elif kapital == 200:
        print("Sie können auch direkt 200 Euro abheben")
    else:
        print("Soviel Geld haben Sie nicht")
else:
    print("Sonst hast du keine anderen Probleme oder?")
    