import random

print("Geben Sie eine ganze oder Kommazahl zwischen 1 und 10 ein: ")
eingabe = input()

# Проверяем, действительно ли введено число (включая float)
try:
    eingabe = float(eingabe)  # преобразуем в число (float)
except ValueError:
    print("Fehlermeldung: Keine gültige Zahl!")
    exit()

# Создаём случайное число с дробной частью
random_number = random.randint(1, 9)  # целая часть
randomnachkomma = random.randint(0, 99)  # дробная часть (0–99)
random_value = randomnachkomma / 100     # превращаем в 0.xx
endergebnis = random_number + random_value

# Показываем для проверки
print(f"Zufallszahl (mit Nachkommastellen): {endergebnis:.2f}")

# Проверяем результат
if eingabe == endergebnis:
    print("Sie haben gewonnen 🎉")
else:
    print(f"Sie haben leider verloren 😞. Die richtige Zahl war {endergebnis:.2f}")
