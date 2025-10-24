
# Menüliste (Dictionary mit Preisangaben)
menu = {
"Pizza": 8.50,
"Pasta": 7.00,
"Salat": 5.50,
"Suppe": 4.00
}

# Küche (Callback-Funktion)
def kitchen(order):
    print(f"[Küche] Bereite {order} zu ... ")
    print(f"[Küche] {order} ist fertig!\n")

# Kellner nimmt Bestellung auf und ruft die Callback-Funktion auf
def waiter(callback):
    print("Willkommen im Restaurant!\nHier ist unser Menü:")
    for dish, price in menu.items():
        print(f"- {dish}: €{price:.2f}")

    order = input("\nWas mochten Sie bestellen? ")

    if order in menu:
        print(f"[Kellner] Sie haben {order} bestellt.")
        callback(order) # Callback wird hier aufgerufen (die Küche)
        print(f"[Kellner] Guten Appetit mit Ihrer {order}!")
    else:
        print(f"[Kellner] Leider haben wir kein {order} auf der Karte.")
        
        print (" Bitte Wählen Sie aus unserem Menü")
    
waiter(kitchen)
