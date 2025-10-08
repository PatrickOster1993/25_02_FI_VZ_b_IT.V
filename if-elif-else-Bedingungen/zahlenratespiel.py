geheime_zahl=75
durchlauf=0
while True:
    durchlauf=durchlauf+1
 
    
    erratene_zahl=int(input("Gebe deine geratene Zahl ein: "))
    
    if erratene_zahl<geheime_zahl:
        print("Die Zahl ist zu niedrig !")
    elif erratene_zahl>geheime_zahl:
        print("Die Zahl ist zu hoch !")
    elif erratene_zahl==geheime_zahl:
        print(f"Glückwunsch du hast die Zahl erraten in {durchlauf} Durchläufen!!!")
        break
 