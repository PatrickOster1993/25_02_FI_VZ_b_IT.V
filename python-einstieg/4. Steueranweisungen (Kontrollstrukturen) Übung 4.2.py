# zu testende Punktzahl
punktzahl = 85

# Bestimmung der Note
if punktzahl >= 90:
    note = "Note 1"
elif punktzahl >= 80:
    # wird nur ausgeführt, wenn die Punktzahl >= 80,  aber  < 90 ist.
    note = "Note 2"
elif punktzahl >= 70:
    # wird nur ausgeführt, wenn die Punktzahl >= 70, aber < 80 ist.
    note = "Note 3"
elif punktzahl >= 60:
    # wird nur ausgeführt, wenn die Punktzahl >= 60, aber also < 70 ist.
    note = "Note 4"
else:
    # Punktzahl < 60
    note = "Note 5"

# Ausgabe des Ergebnisses
print(f"Mit {punktzahl} Punkten erreichen Sie die {note}.")