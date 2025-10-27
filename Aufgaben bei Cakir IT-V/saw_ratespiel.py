from random import randint

print("Wilkommen bei THE SAW, dem Tödlichen Zahlenrätsel \U0001F60A")
print("\n Du hast drei Versuche, die  richtige zahl zwischen 1 und 10 zu erraten")
print("Wenn du die Prüfung nicht schaffst, wirst du eleminiert \U0001F608")


random_number=randint(1,10)
attempts=3

while attempts>0:
    input_value=input(f" Ich möchte ein Spiel spielen, gebe eine Zahl zwischen 1 und 10 ein, du hast jetzt {attempts} versuche frei \U0001F60A")

    if input_value.isdigit():
        input_value=int(input_value)
        if 1<= input_value <=10:
            if input_value==random_number:
                print("\U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A")
                print(" Du hast gewonnen, ich hoffe du lernst aus deinen Fehlern du hast dir dein Leben verdient")
                print("\U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A \U0001F60A")
                break
            else:
                attempts -=1
                if input_value<random_number:
                    print(f" Die Gesuchte Zahl ist Höher")
                elif input_value>random_number:
                    print(f" Die Gesuchte ZZahl ist Kleiner")
                if attempts>0:
                    print(f" Falsch geraten, versuche es nochmal \U0001F480 ")
                else:
                    print("____________________________________________________")
                    print("\n Du hast alle deine Chancen verspielt")
                    print(f"Das war dein finales Spiel. Für dich heißt es Games Over \U0001F480")
                    print(f"Die gesuchte Zahl war {random_number} \U0001F480")
                    print("____________________________________________________")
        else:
            print(" Die Spielegeln lauten Zahlen zwischen 1 und 10 eingeben")
    else:
        print(" Sonst hast du Keine Probleme oder?? Sieht das aus wie eine Zahl")
        attempts -=1
print(" Vielen Dank, das du mitgespielt hast")                            


