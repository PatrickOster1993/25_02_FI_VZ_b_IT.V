dozenten=["jorg","Dirk","Cakir","patrick"]
print(dozenten)
print(" ".join(dozenten)) # Here I convert the list to a string, and it remains this way!
print("|".join(dozenten))  
ausgabe=";".join(dozenten)       
print (f"super Dozenten sind :{str (ausgabe)} nicht war") 

print(ausgabe.split(";"))

einkaufe = ["nudeln", "wasser", "butter", "brot"]
verkaufen = einkaufe 
verkaufen_einkaufe = einkaufe.copy()
print(verkaufen)
verkaufen.append("reis")
print(verkaufen)
print(einkaufe)
print(verkaufen_einkaufe)