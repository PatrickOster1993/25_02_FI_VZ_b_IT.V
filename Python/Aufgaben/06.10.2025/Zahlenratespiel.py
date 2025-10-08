#Zahlenratespiel 

geheime_zahl = 42
versuche = 1
print("Kanst du die Zahl erraten?")

while True:

    print("Rate eine Zahl")
    geraten_zahl = int(input())

    if geraten_zahl == geheime_zahl:
        print("Richtig geraten!")
        print(f"Sie haben {versuche} Versuch(e) gebraucht")
        break
    elif geraten_zahl > geheime_zahl:
        versuche = versuche+1
        print("Ihre Zahl ist zu hoch!")        
    elif geraten_zahl < geheime_zahl:
        versuche = versuche+1
        print("Ihre Zahl ist zu niedrig!")
        