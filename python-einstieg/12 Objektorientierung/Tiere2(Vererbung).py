# --- OBERKLASSE: Tier ---

class Tier:
    """Basisklasse für alle Tiere."""
    def __init__(self, name, art, leben):
        self.name = name
        self.art = art
        self.leben = leben  # Lebenspunkte (integer)
        
    def info(self):
        print("\n--- TIER-INFO ---")
        print(f"Name: {self.name}, Art: {self.art}, Leben: {self.leben}")
        self.status()

    def status(self):
        if self.leben > 0:
            print("Status: Lebt")
        else:
            print("Status: Tot")


# --- UNTERKLASSE: Raubtier (Erbt von Tier) ---

class Raubtier(Tier):
    """Unterklasse, die von Tier erbt und das Attribut Stärke hinzufügt."""
    
    # Der Konstruktor wird überschrieben und ruft den Konstruktor der Oberklasse auf.
    def __init__(self, name, art, leben, staerke):
        # Ruft den Konstruktor der Oberklasse (Tier) auf, um die Basisattribute zu initialisieren
        super().__init__(name, art, leben) 
        
        # Fügt das neue, spezifische Attribut hinzu
        self.staerke = staerke 
        
    # Methode info() wird überschrieben, um die Stärke zusätzlich anzuzeigen
    def info(self):
        # Ruft zuerst die info-Methode der Oberklasse auf (optional, um Code zu sparen)
        super().info() 
        print(f"**Stärke:** {self.staerke}")
        
    # Neue Methode: Angreifen
    def angreifen(self, ziel):
        print(f"\n{self.name} ({self.art}) greift {ziel.name} ({ziel.art}) an!")
        
        # 1. Schadensberechnung (10% der Lebenspunkte des Ziels)
        schaden = ziel.leben * 0.10 
        
        # 2. if-Prüfung: Reduzierung der Lebenspunkte nur, wenn das Ziel noch lebt
        if ziel.leben > 0:
            ziel.leben = ziel.leben - schaden
            
            # Überprüft, ob das Ziel durch den Angriff getötet wurde
            if ziel.leben <= 0:
                 ziel.leben = 0 # Setzt Leben auf 0, falls der Schaden über den Restpunkten lag
                 print(f"FATAL: {ziel.name} hat {schaden:.0f} Schaden erlitten und ist gestorben.")
            else:
                 print(f"{ziel.name} erleidet {schaden:.0f} Schaden. Neues Leben: {ziel.leben:.0f}")
        else:
            print(f"Der Angriff auf {ziel.name} schlägt fehl, da das Ziel bereits tot ist.")


# --- PROGRAMM-SIMULATION ---

# Erstellung einer Instanz der Unterklasse Raubtier (Löwe)
loewe = Raubtier("Simba", "Löwe", 150, 8) 

# Erstellung einer Instanz der Oberklasse Tier (Zebra)
zebra = Tier("Marty", "Zebra", 120) 
maus = Tier("Jolanda", "Maus", 5) # Kleines Tier

# 1. Erste Info-Ausgabe (Löwe ruft die ÜBERSCHRIEBENE Methode auf)
loewe.info()
zebra.info()

# 2. Angriff 1: Löwe greift Zebra an
loewe.angreifen(zebra)
zebra.status() # Status nach dem ersten Angriff

# 3. Angriff 2: Löwe greift Zebra an (Zebra hat nun weniger Leben)
loewe.angreifen(zebra)
zebra.status() # Status nach dem zweiten Angriff

# 4. Angriff 3: Löwe greift die Maus an (führt zum sofortigen Tod)
loewe.angreifen(maus)
maus.status() # Maus ist nun tot