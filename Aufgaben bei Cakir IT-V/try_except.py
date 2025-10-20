#print("Bitte gebe eine Zahl ein   ")
#z=input()#zunächst Eingabe bzw Zahl als String gespeichert
#zahl=int(z) #hier findet Convert oder Parsing statt

#print(f"Sie haben die Ganze Zahl {zahl} eingegeben")


#print("Bitte gebe eine Zahl ein   ")
#z=input()

#try:
#    zahl=int(z)
#    print(f"Sie haben die Gnaze Zahl {zahl} eingegeben")
#except:
#    print("Du hast keine Zahl eingegeben")   


try:
    zahl=int(input("Gib doch bitte eine Zahl ein:  "))
    ergebnis=10/zahl
    print("Ergebnis", ergebnis)
except ZeroDivisionError:
    print("Fehler: Durch 0 kann man nicht teilen")
except ValueError:
    print("Fehler bitte gebe eine Gültige Zahl ein")
        
