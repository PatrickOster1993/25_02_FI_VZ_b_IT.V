# 6.1: Additions-Funktion

print("\n++++++++++++++++Addierer++++++++++++++++")
print("(Bitte geben sie nur ganze Zahlen ein!)")

x = input("\nBitte geben sie ihre ersete Zahl ein: ")
y = input("\nBitte geben sie ihre zweite Zahl ein: ")

if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
else:
    print("\nKeine korrekte Eingabe, starten sie das Programm neu!")
    print("")
    quit()


def addiere(x,y):
    x+y
    return x+y

ergebniss = addiere(x,y)

print(f"\nDas Ergebniss ist: {ergebniss}")    
print("")
