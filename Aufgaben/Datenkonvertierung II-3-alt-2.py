# Altersumrechnung 

print("")

alter = input("Wie viele Jahre sind sie alt?: ")

try:
    int(alter)
except ValueError:
    alter = input("Bitte geben sie eine ganze Zahl für ihr Alter ein: ")

try:
    int(alter)
except ValueError:    
    print("Wieder Falsch bitte starten sie das Programm neu")
    quit()

monate = int(alter)*12

print("")
print(f"Sie sind somit {monate} Monate alt")
print("")
