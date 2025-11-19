import pygame
import random
import sys

# Initialisierung
pygame.init()

# Konstanten
BREITE = 800
HOEHE = 600
FPS = 60

# Farben
WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
GELB = (255, 255, 0)
GRAU = (128, 128, 128)
DUNKELGRAU = (50, 50, 50)

# Straßen-Parameter
STRASSE_BREITE = 400
STRASSE_X = (BREITE - STRASSE_BREITE) // 2
FAHRBAHN_LINIE_BREITE = 10
FAHRBAHN_LINIE_HOEHE = 40


class Auto:
    """Spieler-Auto"""
    def __init__(self, x, y):
        self.breite = 50
        self.hoehe = 100
        self.x = x
        self.y = y
        self.geschwindigkeit = 0
        self.max_geschwindigkeit = 8
        self.beschleunigung = 0.3
        self.reibung = 0.1
        self.lenk_geschwindigkeit = 5
        
    def bewegen(self, keys):
        """Bewegung basierend auf Tasteneingaben"""
        # Beschleunigung
        if keys[pygame.K_UP]:
            self.geschwindigkeit = min(self.geschwindigkeit + self.beschleunigung, 
                                       self.max_geschwindigkeit)
        elif keys[pygame.K_DOWN]:
            self.geschwindigkeit = max(self.geschwindigkeit - self.beschleunigung, 
                                       -self.max_geschwindigkeit / 2)
        else:
            # Reibung anwenden
            if self.geschwindigkeit > 0:
                self.geschwindigkeit = max(0, self.geschwindigkeit - self.reibung)
            elif self.geschwindigkeit < 0:
                self.geschwindigkeit = min(0, self.geschwindigkeit + self.reibung)
        
        # Lenkung
        if keys[pygame.K_LEFT]:
            self.x -= self.lenk_geschwindigkeit
        if keys[pygame.K_RIGHT]:
            self.x += self.lenk_geschwindigkeit
        
        # Grenzen überprüfen
        if self.x < STRASSE_X + 20:
            self.x = STRASSE_X + 20
        if self.x > STRASSE_X + STRASSE_BREITE - self.breite - 20:
            self.x = STRASSE_X + STRASSE_BREITE - self.breite - 20
    
    def zeichnen(self, screen):
        """Auto zeichnen"""
        # Hauptkarosserie
        pygame.draw.rect(screen, ROT, (self.x, self.y, self.breite, self.hoehe))
        # Windschutzscheibe
        pygame.draw.rect(screen, BLAU, (self.x + 5, self.y + 10, self.breite - 10, 25))
        # Räder
        pygame.draw.rect(screen, SCHWARZ, (self.x - 5, self.y + 15, 10, 20))
        pygame.draw.rect(screen, SCHWARZ, (self.x + self.breite - 5, self.y + 15, 10, 20))
        pygame.draw.rect(screen, SCHWARZ, (self.x - 5, self.y + 65, 10, 20))
        pygame.draw.rect(screen, SCHWARZ, (self.x + self.breite - 5, self.y + 65, 10, 20))
        # Lichter
        pygame.draw.circle(screen, GELB, (int(self.x + 12), int(self.y + 95)), 5)
        pygame.draw.circle(screen, GELB, (int(self.x + self.breite - 12), int(self.y + 95)), 5)
    
    def get_rect(self):
        """Gibt das Rechteck für Kollisionserkennung zurück"""
        return pygame.Rect(self.x, self.y, self.breite, self.hoehe)


class GegnerAuto:
    """Gegnerisches Auto"""
    def __init__(self, x, y, geschwindigkeit):
        self.breite = 50
        self.hoehe = 100
        self.x = x
        self.y = y
        self.geschwindigkeit = geschwindigkeit
        self.farbe = random.choice([BLAU, GRUEN, GELB, GRAU])
    
    def bewegen(self, spieler_geschwindigkeit):
        """Bewegt das Gegner-Auto"""
        self.y += spieler_geschwindigkeit + self.geschwindigkeit
    
    def zeichnen(self, screen):
        """Gegner-Auto zeichnen"""
        pygame.draw.rect(screen, self.farbe, (self.x, self.y, self.breite, self.hoehe))
        pygame.draw.rect(screen, DUNKELGRAU, (self.x + 5, self.y + 65, self.breite - 10, 25))
        # Räder
        pygame.draw.rect(screen, SCHWARZ, (self.x - 5, self.y + 15, 10, 20))
        pygame.draw.rect(screen, SCHWARZ, (self.x + self.breite - 5, self.y + 15, 10, 20))
        pygame.draw.rect(screen, SCHWARZ, (self.x - 5, self.y + 65, 10, 20))
        pygame.draw.rect(screen, SCHWARZ, (self.x + self.breite - 5, self.y + 65, 10, 20))
        # Rücklichter
        pygame.draw.circle(screen, ROT, (int(self.x + 12), int(self.y + 5)), 5)
        pygame.draw.circle(screen, ROT, (int(self.x + self.breite - 12), int(self.y + 5)), 5)
    
    def get_rect(self):
        """Gibt das Rechteck für Kollisionserkennung zurück"""
        return pygame.Rect(self.x, self.y, self.breite, self.hoehe)


class Rennspiel:
    """Hauptspiel-Klasse"""
    def __init__(self):
        self.screen = pygame.display.set_mode((BREITE, HOEHE))
        pygame.display.set_caption("🏎️ Python Autorennspiel")
        self.clock = pygame.time.Clock()
        self.font_gross = pygame.font.Font(None, 72)
        self.font_mittel = pygame.font.Font(None, 48)
        self.font_klein = pygame.font.Font(None, 36)
        
        # Spielvariablen
        self.spieler = Auto(BREITE // 2 - 25, HOEHE - 150)
        self.gegner = []
        self.punkte = 0
        self.level = 1
        self.strassen_offset = 0
        self.spiel_aktiv = False
        self.pause = False
        self.game_over = False
        self.highscore = 0
    
    def neues_spiel(self):
        """Startet ein neues Spiel"""
        self.spieler = Auto(BREITE // 2 - 25, HOEHE - 150)
        self.gegner = []
        self.punkte = 0
        self.level = 1
        self.strassen_offset = 0
        self.spiel_aktiv = True
        self.pause = False
        self.game_over = False
    
    def gegner_erstellen(self):
        """Erstellt neue Gegner-Autos"""
        if len(self.gegner) < 3 + self.level:
            if random.randint(0, 100) < 2:
                # Zufällige Fahrbahnposition
                fahrbahn_positionen = [
                    STRASSE_X + 50,
                    STRASSE_X + STRASSE_BREITE // 2 - 25,
                    STRASSE_X + STRASSE_BREITE - 100
                ]
                x = random.choice(fahrbahn_positionen)
                geschwindigkeit = random.uniform(1, 2 + self.level * 0.3)
                self.gegner.append(GegnerAuto(x, -150, geschwindigkeit))
    
    def kollision_pruefen(self):
        """Prüft Kollisionen"""
        spieler_rect = self.spieler.get_rect()
        for gegner in self.gegner:
            if spieler_rect.colliderect(gegner.get_rect()):
                return True
        return False
    
    def zeichne_strasse(self):
        """Zeichnet die Straße mit Animation"""
        # Hintergrund (Gras)
        self.screen.fill(GRUEN)
        
        # Straße
        pygame.draw.rect(self.screen, DUNKELGRAU, 
                        (STRASSE_X, 0, STRASSE_BREITE, HOEHE))
        
        # Straßenränder
        pygame.draw.rect(self.screen, WEISS, 
                        (STRASSE_X, 0, 15, HOEHE))
        pygame.draw.rect(self.screen, WEISS, 
                        (STRASSE_X + STRASSE_BREITE - 15, 0, 15, HOEHE))
        
        # Mittellinie (animiert)
        self.strassen_offset += self.spieler.geschwindigkeit
        if self.strassen_offset > FAHRBAHN_LINIE_HOEHE * 2:
            self.strassen_offset = 0
        
        for y in range(-FAHRBAHN_LINIE_HOEHE * 2, HOEHE, FAHRBAHN_LINIE_HOEHE * 2):
            pygame.draw.rect(self.screen, GELB,
                           (STRASSE_X + STRASSE_BREITE // 2 - FAHRBAHN_LINIE_BREITE // 2,
                            y + self.strassen_offset,
                            FAHRBAHN_LINIE_BREITE,
                            FAHRBAHN_LINIE_HOEHE))
    
    def zeichne_ui(self):
        """Zeichnet UI-Elemente"""
        # Punkte
        punkte_text = self.font_klein.render(f"Punkte: {self.punkte}", True, WEISS)
        self.screen.blit(punkte_text, (20, 20))
        
        # Level
        level_text = self.font_klein.render(f"Level: {self.level}", True, WEISS)
        self.screen.blit(level_text, (20, 60))
        
        # Highscore
        highscore_text = self.font_klein.render(f"Highscore: {self.highscore}", True, WEISS)
        self.screen.blit(highscore_text, (20, 100))
        
        # Geschwindigkeitsanzeige
        geschwindigkeit_kmh = int(abs(self.spieler.geschwindigkeit) * 15)
        geschw_text = self.font_klein.render(f"Geschwindigkeit: {geschwindigkeit_kmh} km/h", 
                                             True, GELB)
        self.screen.blit(geschw_text, (BREITE - 350, 20))
        
        # Tacho-Balken
        tacho_breite = 200
        tacho_hoehe = 30
        tacho_x = BREITE - 350
        tacho_y = 70
        pygame.draw.rect(self.screen, WEISS, 
                        (tacho_x, tacho_y, tacho_breite, tacho_hoehe), 2)
        geschw_prozent = min(abs(self.spieler.geschwindigkeit) / self.spieler.max_geschwindigkeit, 1)
        if geschw_prozent > 0:
            farbe = GRUEN if geschw_prozent < 0.7 else GELB if geschw_prozent < 0.9 else ROT
            pygame.draw.rect(self.screen, farbe,
                           (tacho_x + 2, tacho_y + 2, 
                            int((tacho_breite - 4) * geschw_prozent), tacho_hoehe - 4))
    
    def zeichne_startscreen(self):
        """Zeichnet den Startbildschirm"""
        self.screen.fill(DUNKELGRAU)
        
        titel = self.font_gross.render("AUTORENNSPIEL", True, GELB)
        titel_rect = titel.get_rect(center=(BREITE // 2, HOEHE // 3))
        self.screen.blit(titel, titel_rect)
        
        anleitung = [
            "STEUERUNG:",
            "← → : Lenken",
            "↑ : Beschleunigen",
            "↓ : Bremsen",
            "LEERTASTE: Pause",
            "",
            "Drücke ENTER zum Starten",
            "Drücke ESC zum Beenden"
        ]
        
        y = HOEHE // 2
        for zeile in anleitung:
            text = self.font_klein.render(zeile, True, WEISS)
            text_rect = text.get_rect(center=(BREITE // 2, y))
            self.screen.blit(text, text_rect)
            y += 40
    
    def zeichne_pause(self):
        """Zeichnet Pause-Overlay"""
        overlay = pygame.Surface((BREITE, HOEHE))
        overlay.set_alpha(128)
        overlay.fill(SCHWARZ)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_gross.render("PAUSE", True, GELB)
        pause_rect = pause_text.get_rect(center=(BREITE // 2, HOEHE // 2))
        self.screen.blit(pause_text, pause_rect)
        
        info_text = self.font_klein.render("Drücke LEERTASTE zum Fortsetzen", True, WEISS)
        info_rect = info_text.get_rect(center=(BREITE // 2, HOEHE // 2 + 80))
        self.screen.blit(info_text, info_rect)
    
    def zeichne_gameover(self):
        """Zeichnet Game Over Bildschirm"""
        overlay = pygame.Surface((BREITE, HOEHE))
        overlay.set_alpha(200)
        overlay.fill(SCHWARZ)
        self.screen.blit(overlay, (0, 0))
        
        gameover_text = self.font_gross.render("GAME OVER!", True, ROT)
        gameover_rect = gameover_text.get_rect(center=(BREITE // 2, HOEHE // 3))
        self.screen.blit(gameover_text, gameover_rect)
        
        punkte_text = self.font_mittel.render(f"Punkte: {self.punkte}", True, WEISS)
        punkte_rect = punkte_text.get_rect(center=(BREITE // 2, HOEHE // 2))
        self.screen.blit(punkte_text, punkte_rect)
        
        if self.punkte > self.highscore:
            neuer_rekord = self.font_klein.render("NEUER HIGHSCORE!", True, GELB)
            rekord_rect = neuer_rekord.get_rect(center=(BREITE // 2, HOEHE // 2 + 60))
            self.screen.blit(neuer_rekord, rekord_rect)
        
        restart_text = self.font_klein.render("Drücke ENTER für Neustart", True, WEISS)
        restart_rect = restart_text.get_rect(center=(BREITE // 2, HOEHE - 100))
        self.screen.blit(restart_text, restart_rect)
    
    def spiel_loop(self):
        """Hauptspiel-Schleife"""
        laeuft = True
        
        while laeuft:
            self.clock.tick(FPS)
            
            # Event-Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    laeuft = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        laeuft = False
                    
                    if not self.spiel_aktiv and not self.game_over:
                        if event.key == pygame.K_RETURN:
                            self.neues_spiel()
                    
                    if self.spiel_aktiv:
                        if event.key == pygame.K_SPACE:
                            self.pause = not self.pause
                    
                    if self.game_over:
                        if event.key == pygame.K_RETURN:
                            self.neues_spiel()
            
            # Startbildschirm
            if not self.spiel_aktiv and not self.game_over:
                self.zeichne_startscreen()
            
            # Spiellogik
            elif self.spiel_aktiv and not self.pause and not self.game_over:
                keys = pygame.key.get_pressed()
                
                # Spieler bewegen
                self.spieler.bewegen(keys)
                
                # Gegner erstellen
                self.gegner_erstellen()
                
                # Gegner bewegen
                for gegner in self.gegner[:]:
                    gegner.bewegen(self.spieler.geschwindigkeit)
                    
                    # Entferne Gegner, die außerhalb sind
                    if gegner.y > HOEHE:
                        self.gegner.remove(gegner)
                        self.punkte += 10
                        
                        # Level erhöhen
                        if self.punkte % 100 == 0:
                            self.level += 1
                
                # Kollisionsprüfung
                if self.kollision_pruefen():
                    self.game_over = True
                    if self.punkte > self.highscore:
                        self.highscore = self.punkte
                
                # Zeichnen
                self.zeichne_strasse()
                
                # Gegner zeichnen
                for gegner in self.gegner:
                    gegner.zeichnen(self.screen)
                
                # Spieler zeichnen
                self.spieler.zeichnen(self.screen)
                
                # UI zeichnen
                self.zeichne_ui()
            
            # Pause
            elif self.pause:
                self.zeichne_strasse()
                for gegner in self.gegner:
                    gegner.zeichnen(self.screen)
                self.spieler.zeichnen(self.screen)
                self.zeichne_ui()
                self.zeichne_pause()
            
            # Game Over
            elif self.game_over:
                self.zeichne_strasse()
                for gegner in self.gegner:
                    gegner.zeichnen(self.screen)
                self.spieler.zeichnen(self.screen)
                self.zeichne_ui()
                self.zeichne_gameover()
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()


def main():
    """Hauptfunktion"""
    print("=" * 50)
    print("🏎️  PYTHON AUTORENNSPIEL")
    print("=" * 50)
    print("\nStarte das Spiel...")
    print("\nViel Spaß beim Spielen! 🏁")
    
    spiel = Rennspiel()
    spiel.spiel_loop()


if __name__ == "__main__":
    main()