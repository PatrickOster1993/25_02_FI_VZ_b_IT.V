schueler0="Möller"
schueler1="Ohletz"
schueler2="Schulze"
schueler3="Goebel"
#               0        1        2         3     4
umschueler=["Möller","Ohletz","Schulze","Goebel",10]#hiermit habe ich mehrere Werte in einer Variable gespeichert
print(umschueler)
umschueler.append("Cakir")#fügt einen weiteren Wert in die Liste ein
print(umschueler)

#print("Beim den Umschülern handelt es sich um",type(umschuler))
#       0,1,2,3,4
#tupel=(1,2,3,4,5)
#tupel=(0)=5
#print(tupel)

liste=[1,2,3,4,5]
liste[0]=5
print(liste)



print(len(umschueler))#len zählt die Anzahl der Elemente in der Liste
print(umschueler[0])#gibt das erste Element der Liste aus
print(umschueler[4])#gibt das fünfte Element der Liste aus
print(umschueler[-1])#gibt das letzte Element der Liste aus
print(umschueler[-2])#gibt das vorletzte Element der Liste aus
print(umschueler[1:3])#gibt die Elemente 1 bis 2 aus (3 ist ausgeschlossen)
print(umschueler[1:])#gibt die Elemente 1 bis zum Ende aus
print(umschueler[:3])#gibt die Elemente von Anfang bis 2 aus (3 ist ausgeschlossen)             
umschueler.remove("Goebel")#entfernt den Eintrag "Goebel" aus der Liste
print(umschueler)
umschueler.pop()#entfernt das letzte Element der Liste
print(umschueler)
umschueler.pop(0)#entfernt das erste Element der Liste  
print(umschueler)
umschueler.insert(0,"Goebel")#fügt "Goebel" an  der ersten Position ein
print(umschueler)               
umschueler.insert(2,"Müller")#fügt "Müller" an  der dritten Position ein
print(umschueler)   
umschueler[4]=15#ändert den Wert an der fünften Position auf 15
print(umschueler)
umschueler[0]="Möller"#ändert den Wert an der ersten Position auf "Möller"  
print(umschueler)
umschueler.sort#sortiert die Liste alphabetisch bzw. aufsteigend      
print(umschueler)   
umschueler.reverse()#kehrt die Reihenfolge der Liste um
print(umschueler)   
umschueler.clear()#löscht alle Elemente der Liste
print(umschueler)
umschueler=["Möller","Ohletz","Schulze","Goebel",10]
print(umschueler)   
umschueler.extend(["Cakir","Neumann"])#fügt mehrere Elemente an das Ende der Liste an
print(umschueler)   
print(umschueler.index("Schulze"))#gibt die Position des Eintrags "Schulze" aus
print(umschueler.count("Möller"))#zählt, wie oft "  Möller" in der Liste vorkommt   
print(umschueler)   
umschueler2=umschueler.copy()#erstellt eine Kopie der Liste
print(umschueler2)  
print(umschueler)
print(umschueler2)
print(id(umschueler))#gibt die Speicheradresse der Liste aus
print(id(umschueler2))#gibt die Speicheradresse der Kopie der Liste aus
umschueler2[0]="Test"#ändert den Wert an der ersten Position der Kopie auf "Test"
print(umschueler)
print(umschueler2)  
print(id(umschueler))#gibt die Speicheradresse der Liste aus
print(id(umschueler2))#gibt die Speicheradresse der Kopie der Liste aus 
#listen sind veränderbar, tupel nicht
tupel=("Möller","Ohletz","Schulze","Goebel",10)
print(tupel)    
print(tupel[0])#gibt das erste Element des Tupels aus
print(tupel[-1])#gibt das letzte Element des Tupels aus
print(tupel[1:3])#gibt die Elemente 1 bis 2 aus (3 ist ausgeschlossen)
print(tupel[1:])#gibt die Elemente 1 bis zum Ende aus
print(tupel[:3])#gibt die Elemente von Anfang bis 2 aus (       3 ist ausgeschlossen)             
print(len(tupel))#len zählt die Anzahl der Elemente im Tupel        
print(tupel.count("Möller"))#zählt, wie oft "  Möller" im Tupel vorkommt
print(tupel.index("Schulze"))#gibt die Position des Eintrags "Schulze" aus
print(type(tupel))#gibt den Datentyp aus        
#tupel[0]="Test"#führt zu einem Fehler, da Tupel nicht veränderbar sind         
#tupel.append("Test")#führt zu einem Fehler, da Tupel nicht veränderbar sind         
#tupel.remove("Möller")#führt zu einem Fehler, da Tupel nicht veränderbar sind              
#tupel.pop()#führt zu einem Fehler, da Tupel nicht veränderbar sind         
#tupel.clear()#führt zu einem Fehler, da Tupel nicht veränderbar sind         
#tupel.sort()#führt zu einem Fehler, da Tupel nicht veränderbar sind         
#tupel.reverse()#führt zu einem Fehler, da Tupel nicht veränderbar  sind        
#tupel.insert(0,"Test")#führt zu einem Fehler, da Tupel nicht veränderbar sind          
#tupel.extend(["Test1","Test2"])#führt zu einem Fehler, da Tupel nicht veränderbar sind         
tupel2=list(tupel)#wandelt das Tupel in eine Liste um       
print(tupel2)
print(type(tupel2))#gibt den Datentyp aus           
tupel2[0]="Test"#ändert den Wert an der ersten Position der Liste auf "Test"
print(tupel2)
print(type(tupel))#gibt den Datentyp aus    
print(type(tupel2))#gibt den Datentyp aus   
tupel3=tuple(tupel2)#wandelt die Liste wieder in ein Tupel um       
print(tupel3)               
print(type(tupel3))#gibt den Datentyp aus               
#tupel3[0]="Test2"#führt zu einem Fehler, da Tupel nicht veränderbar sind           
print(tupel3)           
print(type(tupel3))#gibt den Datentyp aus           
liste2=list(tupel)#wandelt das Tupel in eine Liste um       
print(liste2)
print(type(liste2))#gibt den Datentyp aus           
liste2[0]="Test3"#ändert den Wert an der ersten Position der Liste auf "Test3"
print(liste2)                           
print(type(liste2))#gibt den Datentyp aus   
liste3=tuple(liste2)#wandelt die Liste wieder in ein Tupel um       
print(liste3)
print(type(liste3))#gibt den Datentyp aus               
#liste3[0]="Test4"#führt zu einem Fehler, da Tupel nicht veränderbar sind       
print(liste3)           
print(type(liste3))#gibt den Datentyp aus
#       0,1,2,3,4
#tupel=(1,2,3,4,5)      
#tupel=(0)=5
#print(tupel)   

#liste=[1,2,3,4,5]
#liste[0]=5 
#print(liste)





