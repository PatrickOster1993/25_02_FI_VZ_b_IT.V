import random

print("Geben Sie einen ganze Zahl einzwichen 1 und 10 ein: ")
eingabe=input()#hie steckt ihre Eingabe als String vorerst
if eingabe.isdigit():#prüft ob die Eingabe tatsächlich eine Zahl war #true
    eingabe=int(eingabe)#bei Zahl dann konvertiere
    random_number=random.randint(1,10)##stekt eine Zufallszahl in random_number
   
    if eingabe==random_number:
        print("Sie haben gewonnen")
        print("      :-")
        print("--------------")
    else:
       print(f"Sie haben leider verloren die Zahl war {random_number}")
        
else:
       print("Sonst ghets dir gut oder?! War keine gültige Zahl")

print("Danke hoffe Ihnen hat mein Quellcode gefallen")
       