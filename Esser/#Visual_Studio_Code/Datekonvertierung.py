a = "5"
b = "7"
print(a+b)
print("")
        #       Konvertierung       #
print(int(a)+int(b))
        #       Konvertierung       #       String Literal        #
print(f"{int(a)+int(b)}")
print("")
        #       Kovertierung        #       Float       #
kommazahl = "3.16852"
kommazahl_2 = "6.89432"
print(kommazahl+kommazahl_2)
print(f"{float(kommazahl)+float(kommazahl_2)}")
print("")
        #       Konvertierung       #       Nachträglich definiert      #
a="7.2"
b= 5
e= float(a) + b
print(e)
print("")
        #       Konvertierung       #       zahl zu String      #
alter = 39.9
print("ich bin aktuell " +str(alter)+ " Jahre alt")
print("")
        #       Konvertierung       #       Liste zu String      #
dozenten = ["Jörg","Dirk","Cakir","Holger","Christopher","Christian","Patrick"]
print(dozenten)
print("Wird durch die Join-Fuktion zu:")
print(", ".join(dozenten))
ausgabe = (", ".join(dozenten))
print(f"Diese Ausgabe ist die Empfehlung des Dozenten {ausgabe}")
print("Herrlich diese Dozenten "+str(ausgabe)+" nicht wahr")
print("herrlich diese wunderbaren Dozenten "+ausgabe+" oder???",ausgabe)
print("")
honululu = "Hans,Klaus,SoerenAyna, Daisterjaschonwieder, Jetztgehtdaslangsamlos, usw"
print(honululu.split(","))
print("")
einkaufen = ["nudeln","brot","eier","kaese","garnelen"]
print(einkaufen)
verkaufen = einkaufen
print(verkaufen)
verkaufen.append("nudelsoße") 
print(verkaufen)
print(einkaufen)
print("")
verkaufen = einkaufen.copy()
print(verkaufen)