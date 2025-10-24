import random

geheimnis=random.randint(0,1000)
versuche=0
while True:
    try:
        versuch=int(input("Rate bitte einmal von 0 bis 1000"))
    except ValueError:
        print("Das war keine Zahl, also gebe bitte eine Zahl ein")
        continue

    
    if versuch==0:
        print("Das spiel ist zuende")
        break
    versuche+=1

    if versuch<geheimnis:
        print("Die Zahl ist zu klein, versuche es nocheinmal")
    elif versuch>geheimnis:
        print("Die Zahl ist zu gross, versuche es noch einmal")
    else:
        print("Herzlichen Glückwunsch, du hast die zahl erraten")
        print(f"Sie haben so oft {versuche} gebraucht um die Zahl zu erraten")
        break                