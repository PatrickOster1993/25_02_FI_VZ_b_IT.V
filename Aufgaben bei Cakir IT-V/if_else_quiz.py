from random import randint

print("Geben sie bitte eine Zahl zwischen 1 und 10 ein: ")

input_value=input()
if input_value.isdigit():
    input_value=int(input_value)
    random_number=randint(1,10)
    if input_value==random_number:
        print("------------------------------------------------------------------------")
        print("---------Gratuliere sie haben gewonnen, hier dein Döner-----------------")
        print("------------------------------------------------------------------------")
    else:
        print("Sie haben verloren")
        print(f"Die Zufallszahl war {random_number}")
else:
    print("Schlaumeier das war keine gültige Zahl")
print("Danke das du mitgespielt hast")                

