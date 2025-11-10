class Tier:
    # Der Konstruktor: Wird beim Erstellen eines neuen Tier-Objekts aufgerufen
    # Die Methode initialisiert die Attribute (Name, Art, Leben)
    def __init__(self, name, art, leben):
        self.name = name
        self.art = art
        self.leben = leben  # Lebenspunkte
        
    # Gibt alle Basisinformationen aus (Info)
    def info(self):
        print("\n--- TIER-INFORMATIONEN ---")
        print(f"Name: {self.name}")
        print(f"Art: {self.art}")
        print(f"Lebenspunkte: {self.leben}")
        self.status() # Ruft die Statusprüfung direkt auf

    # Prüft, ob das Tier lebt oder tot ist (Status)
    def status(self):
        # Prüfung mit if-else-Struktur
        if self.leben > 0:
            print("Status: Lebt")
        else:
            print("Status: Tot")

# --- ERZEUGEN UND NUTZEN DER OBJEKTE (Instanzen) ---

# Objekte erstellen (Instanziierung der Klasse Tier)
hund = Tier("Bello", "Hund", 100)
katze = Tier("Mietzi", "Katze", 85)
vogel = Tier("Zwitscher", "Vogel", 0) # Vogel ist direkt tot

print("--- ERSTES BERICHTERSTATTUNG ---")

# info() Methode für jedes Objekt aufrufen
hund.info()
katze.info()
vogel.info()

# --- SIMULATION: Lebenspunkte verändern und Status prüfen ---

print("\n--- ZWEITE BERICHTERSTATTUNG (NACH VERÄNDERUNG) ---")

# Beispiel: Der Hund verliert Lebenspunkte
hund.leben = hund.leben - 30 

# Der Hund erhält eine neue Info-Ausgabe mit Statusprüfung
print(f"\n{hund.name} hat 30 Lebenspunkte verloren.")
hund.info()

# Beispiel: Die Katze stirbt (Leben = 0 oder weniger)
katze.leben = -5
katze.status() # Direkter Aufruf der Status-Methode

print("--- PROGRAMM ENDE ---")