print("Punktzahl eingeben")
p=input()

eingabe=int(p)
if 90 <= eingabe <=100:
    print("Note 1")
elif 80 <= eingabe <= 89:
    print("Note 2")
elif 70 <= eingabe <=79:
    print("Note 3")
elif 60 <= eingabe <=69: 
    print("Note 4")
elif 0 <= eingabe <=59: 
    print("Note 5")
else:
    print("Eingabe ungültig nur Zahlen von 0-100 eingeben.")