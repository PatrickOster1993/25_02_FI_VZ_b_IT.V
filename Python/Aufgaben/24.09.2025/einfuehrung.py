Multiplikator=2
Eingabe=input("Wollen sie eine Ganzzahl verdoppeln?")
while Eingabe != str("Nein"):
    
    Eingabe=input("Zahl Eingeben")
    if Eingabe==str("End"): quit
    Ergebnis=int(Eingabe)*int(Multiplikator)
    print(Ergebnis)
    
