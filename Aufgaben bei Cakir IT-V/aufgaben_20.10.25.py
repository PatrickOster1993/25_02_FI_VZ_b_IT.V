#start=0
#while start <11:
#    print(start)
#    start+=1

#aufgabe2

#summe = 1
#ergebniss = 0
#while ergebniss <= 50:
#    ergebniss=2*summe   
#    
#    print(f"2 x {summe}={ergebniss}")
#    summe+=1


#Zahl=int (input("Gebe hier ein Positive Zahl ein"))
#durchschnitt=int (input("geben sie die anzahl der Ziffern ein"))
#ergebniss=Zahl/durchschnitt
#while ergebniss>=0:
#    print("Happy Birthday du otto du hast aufgepasst")
#    break
#else:
#    print("Du spacken pass doch besser auf und hol dir ein klömbschen")    
   








print("Bitte registrieren Sie sich zunächst.")
name = input("Wie heißen Sie? ")
passwort = input(f"Hey {name}, bitte leg jetzt ein Passwort fest: ")
counter=3
print("Registrierung erfolgreich! Jetzt nur noch einloggen. ")
 
while counter>0:
    login_name = input("Benutzername: ")
    login_passwort = input("Passwort: ")
 
    if login_name == name and login_passwort == passwort:
        print(f"Herzlich Willkommen, {name}!")
        break
    counter=-1 

else:
        print("Falscher Benutzername oder Passwort!")
counter=counter+1 
