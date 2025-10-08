import random

print("Geben sie eine Ganze Zahl zwischen 1 und 10 ein:")
eingabe=input()

if eingabe.isdigit():#prüft ob die Eingabe eine Zahl war #true
    eingabe=int(eingabe)# bei Zahl dann Konvertiere
    random_number=random.randint(1,10)
    if eingabe==random_number:
        print("Sie haben gewonnen")
    else:
        print(f"Leider verloren, die Zahl war {random_number}")
else:      
    print("Sonst geht es dir Gut oder?! Das war keine Gültige Zahl")
print("Danke hoffe ihnen hat mein Quellcode gefallen")    
