# Übung 4.2: Notensystem 

print("")

punktzahl  = int(input("Bitte geben sie hier die anzahl der erreichten Punkte ein: "))

print("")

if punktzahl >= 90:
    print("Sie haben die Note 1")
elif punktzahl < 90 and punktzahl >= 80:
    print("Sie haben die Note 2")
elif punktzahl < 80 and punktzahl >= 70:
    print("Sie haben die Note 3")
elif punktzahl <70 and punktzahl >= 60:
    print("Sie habe die Note 4")
else:
    print("Sie haben die Note 5")

print("")
