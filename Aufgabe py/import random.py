import random
print ("Geben sie eime ganz zahl din zwichen 1 und 10 ein : ")
eingabe=input() # hie stekt ihre eingabe als String

if eingabe.isdigit(): # prüfet ob die eingabe  tatsächlich eine zagl war #true
    eingabe=int(eingabe) # bei zahl dann Konvertiere 
    random_number=random.randint(1,10)
    
    if eingabe ==random_number:
        print ("Sie haben gewonnen ")
        print ("   :-)   ")
        print ("-----------")
    else:
        print(f"sie habe leider verloren die zahl war {random_number}") 
else:
    print ("Somnst ghts dir gut oder ? war keine gültige zahl")         
    
      
        