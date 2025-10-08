zahl=(input("Gebe eine Zahl von 1 und 10 ein: "))

if zahl.isdigit():
    zahl=int(zahl)
    import random
    random_number=random.randint(1,10)
    if zahl==random_number:
        print("Herzlichen Glückwunsch du hast die richtige Zahl!")
    else:
        print(f"Leider nicht die richtige Zahl! {random_number} wäre richtig gewesen")

else:
    print("Die Eingabe muss eine Zahl sein !!!")

