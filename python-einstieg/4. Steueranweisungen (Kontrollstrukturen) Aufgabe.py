import random

# Zufällige Zahl zwischen 1 und 100 generieren
geheime_zahl = random.randint(1, 100)


print("Willkommen beim Zahlenratespiel! 🔢")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
print("Sie haben nur EINEN Rateversuch.")

# Benutzer nach geratener Zahl fragen und Typumwandlung mit int()
geratene_zahl_str = input("Geben Sie Ihre Zahl ein: ")

geratene_zahl = int(geratene_zahl_str)

# 3. if-elif-else-Struktur für den Vergleich
if geratene_zahl < geheime_zahl:
    # 3a. Zu niedrig
    print("Ihre Zahl ist zu niedrig!")
    print("Das Spiel ist beendet.")

elif geratene_zahl > geheime_zahl:
    # 3b. Zu hoch
    print("Ihre Zahl ist zu hoch! 📈")
    print("Das Spiel ist beendet.")

else:
    # 3c. Richtig
    print("Richtig geraten! Sie haben gewonnen")

print("\n--- Programm beendet ---")