# Konstante
MONATE_PRO_JAHR = 12

# 1. Eingabe des Alters
print("--- Altersumrechnung: Jahre in Monate ---")

# fragen und die Eingabe in (int) konvertieren.
alter_jahre_str = input("Geben Sie Ihr Alter in Jahren ein: ")
alter_jahre = int(alter_jahre_str)

# 2. Berechnung des Alters in Monaten
# Alter in Monaten = Alter in Jahren * 12
alter_monate = alter_jahre * MONATE_PRO_JAHR

# 3. Ausgabe des umgerechneten Alters
print("\n--- Ergebnis ---")

# Konvertierung der Integer-Werte in String
print("Ihr Alter von " + str(alter_jahre) + " Jahren entspricht:")
print("Alter in Monaten: " + str(alter_monate) + " Monate")
print("----------------")