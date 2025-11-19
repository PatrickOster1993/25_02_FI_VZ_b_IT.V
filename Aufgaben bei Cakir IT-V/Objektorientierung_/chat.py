import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import sys
import datetime


# ==================== SERVER ====================
class ChatServer:
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}  # {socket: username}
        self.aktiv = True
        
    def start(self):
        """Startet den Server"""
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            print("=" * 50)
            print("🖥️  CHAT-SERVER GESTARTET")
            print("=" * 50)
            print(f"Host: {self.host}")
            print(f"Port: {self.port}")
            print("Warte auf Verbindungen...\n")
            
            self.annehmen_thread = threading.Thread(target=self.verbindungen_annehmen)
            self.annehmen_thread.start()
            
        except Exception as e:
            print(f"❌ Fehler beim Starten: {e}")
    
    def verbindungen_annehmen(self):
        """Akzeptiert neue Client-Verbindungen"""
        while self.aktiv:
            try:
                client, address = self.server.accept()
                print(f"🔗 Neue Verbindung von {address}")
                
                thread = threading.Thread(target=self.client_handler, args=(client,))
                thread.start()
            except:
                break
    
    def client_handler(self, client):
        """Behandelt einen einzelnen Client"""
        try:
            # Benutzername empfangen
            username = client.recv(1024).decode('utf-8')
            self.clients[client] = username
            
            print(f"👤 {username} hat den Chat betreten")
            
            # Begrüßungsnachricht
            willkommen = f"SERVER: Willkommen {username}! 🎉"
            client.send(willkommen.encode('utf-8'))
            
            # Andere Benutzer informieren
            self.broadcast(f"SERVER: {username} hat den Chat betreten! 👋", client)
            
            # Benutzerliste senden
            self.benutzerliste_senden()
            
            # Nachrichten empfangen
            while self.aktiv:
                nachricht = client.recv(1024).decode('utf-8')
                if nachricht:
                    print(f"📨 {username}: {nachricht}")
                    
                    # Prüfe auf private Nachricht
                    if nachricht.startswith('/pm '):
                        self.private_nachricht(client, nachricht)
                    else:
                        # Normale Broadcast-Nachricht
                        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                        vollstaendige_nachricht = f"[{timestamp}] {username}: {nachricht}"
                        self.broadcast(vollstaendige_nachricht, client)
                else:
                    break
                    
        except Exception as e:
            print(f"❌ Fehler mit Client {self.clients.get(client, 'Unbekannt')}: {e}")
        finally:
            self.client_entfernen(client)
    
    def broadcast(self, nachricht, sender=None):
        """Sendet Nachricht an alle Clients"""
        for client in list(self.clients.keys()):
            if client != sender:
                try:
                    client.send(nachricht.encode('utf-8'))
                except:
                    self.client_entfernen(client)
    
    def private_nachricht(self, sender, nachricht):
        """Sendet private Nachricht: /pm Username Nachricht"""
        try:
            teile = nachricht.split(' ', 2)
            if len(teile) < 3:
                sender.send("SERVER: Verwendung: /pm Username Nachricht".encode('utf-8'))
                return
            
            ziel_username = teile[1]
            pm_nachricht = teile[2]
            sender_username = self.clients[sender]
            
            # Finde Ziel-Client
            ziel_client = None
            for client, username in self.clients.items():
                if username == ziel_username:
                    ziel_client = client
                    break
            
            if ziel_client:
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                nachricht_ziel = f"[{timestamp}] 💬 PRIVAT von {sender_username}: {pm_nachricht}"
                nachricht_sender = f"[{timestamp}] 💬 PRIVAT an {ziel_username}: {pm_nachricht}"
                
                ziel_client.send(nachricht_ziel.encode('utf-8'))
                sender.send(nachricht_sender.encode('utf-8'))
            else:
                sender.send(f"SERVER: Benutzer '{ziel_username}' nicht gefunden".encode('utf-8'))
                
        except Exception as e:
            sender.send(f"SERVER: Fehler beim Senden der privaten Nachricht".encode('utf-8'))
    
    def benutzerliste_senden(self):
        """Sendet aktuelle Benutzerliste an alle"""
        benutzer = list(self.clients.values())
        liste = "SERVER: 👥 Online: " + ", ".join(benutzer)
        for client in self.clients.keys():
            try:
                client.send(liste.encode('utf-8'))
            except:
                pass
    
    def client_entfernen(self, client):
        """Entfernt Client bei Trennung"""
        if client in self.clients:
            username = self.clients[client]
            del self.clients[client]
            print(f"👋 {username} hat den Chat verlassen")
            self.broadcast(f"SERVER: {username} hat den Chat verlassen 👋")
            self.benutzerliste_senden()
            client.close()
    
    def stop(self):
        """Stoppt den Server"""
        self.aktiv = False
        self.server.close()


# ==================== CLIENT GUI ====================
class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.verbunden = False
        
        # GUI erstellen
        self.window = tk.Tk()
        self.window.title("💬 Python Chat")
        self.window.geometry("700x600")
        self.window.configure(bg='#2c3e50')
        
        self.erstelle_gui()
        
    def erstelle_gui(self):
        """Erstellt die Benutzeroberfläche"""
        # Verbindungsframe (oben)
        verbindung_frame = tk.Frame(self.window, bg='#34495e', pady=10)
        verbindung_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(verbindung_frame, text="Server IP:", 
                bg='#34495e', fg='white', font=('Arial', 10)).grid(row=0, column=0, padx=5)
        self.ip_entry = tk.Entry(verbindung_frame, width=15, font=('Arial', 10))
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(verbindung_frame, text="Port:", 
                bg='#34495e', fg='white', font=('Arial', 10)).grid(row=0, column=2, padx=5)
        self.port_entry = tk.Entry(verbindung_frame, width=8, font=('Arial', 10))
        self.port_entry.insert(0, "5555")
        self.port_entry.grid(row=0, column=3, padx=5)
        
        tk.Label(verbindung_frame, text="Username:", 
                bg='#34495e', fg='white', font=('Arial', 10)).grid(row=0, column=4, padx=5)
        self.username_entry = tk.Entry(verbindung_frame, width=15, font=('Arial', 10))
        self.username_entry.grid(row=0, column=5, padx=5)
        
        self.connect_btn = tk.Button(verbindung_frame, text="Verbinden", 
                                     command=self.verbinden, bg='#27ae60', 
                                     fg='white', font=('Arial', 10, 'bold'),
                                     cursor='hand2')
        self.connect_btn.grid(row=0, column=6, padx=5)
        
        # Chat-Anzeigebereich
        chat_frame = tk.Frame(self.window, bg='#2c3e50')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame, wrap=tk.WORD, state='disabled',
            bg='#ecf0f1', fg='#2c3e50', font=('Arial', 10),
            height=20
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Eingabebereich
        eingabe_frame = tk.Frame(self.window, bg='#34495e', pady=10)
        eingabe_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.nachricht_entry = tk.Entry(
            eingabe_frame, font=('Arial', 11), state='disabled'
        )
        self.nachricht_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.nachricht_entry.bind('<Return>', lambda e: self.sende_nachricht())
        
        self.send_btn = tk.Button(
            eingabe_frame, text="Senden 📤", command=self.sende_nachricht,
            bg='#3498db', fg='white', font=('Arial', 10, 'bold'),
            cursor='hand2', state='disabled'
        )
        self.send_btn.pack(side=tk.RIGHT)
        
        # Info-Bereich
        info_frame = tk.Frame(self.window, bg='#34495e', pady=5)
        info_frame.pack(fill=tk.X, padx=10)
        
        info_text = "💡 Tipp: Verwende /pm Username Nachricht für private Nachrichten"
        tk.Label(info_frame, text=info_text, bg='#34495e', 
                fg='#ecf0f1', font=('Arial', 8)).pack()
        
        # Emoji-Buttons
        emoji_frame = tk.Frame(self.window, bg='#34495e', pady=5)
        emoji_frame.pack(fill=tk.X, padx=10)
        
        emojis = ['😊', '😂', '❤️', '👍', '🎉', '🔥', '✨', '💯']
        for emoji in emojis:
            btn = tk.Button(emoji_frame, text=emoji, 
                          command=lambda e=emoji: self.emoji_einfuegen(e),
                          bg='#34495e', fg='white', font=('Arial', 12),
                          cursor='hand2', state='disabled')
            btn.pack(side=tk.LEFT, padx=2)
            # Emoji-Buttons für später speichern
            if not hasattr(self, 'emoji_buttons'):
                self.emoji_buttons = []
            self.emoji_buttons.append(btn)
        
        self.window.protocol("WM_DELETE_WINDOW", self.beim_schliessen)
        
    def emoji_einfuegen(self, emoji):
        """Fügt Emoji in Textfeld ein"""
        self.nachricht_entry.insert(tk.END, emoji)
        self.nachricht_entry.focus()
    
    def verbinden(self):
        """Verbindet zum Server"""
        if self.verbunden:
            messagebox.showwarning("Warnung", "Bereits verbunden!")
            return
        
        host = self.ip_entry.get()
        port = int(self.port_entry.get())
        username = self.username_entry.get().strip()
        
        if not username:
            messagebox.showerror("Fehler", "Bitte Username eingeben!")
            return
        
        try:
            self.client.connect((host, port))
            self.client.send(username.encode('utf-8'))
            self.verbunden = True
            
            # GUI anpassen
            self.nachricht_entry.config(state='normal')
            self.send_btn.config(state='normal')
            self.connect_btn.config(state='disabled')
            self.ip_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.username_entry.config(state='disabled')
            
            # Emoji-Buttons aktivieren
            for btn in self.emoji_buttons:
                btn.config(state='normal')
            
            # Thread zum Empfangen starten
            empfang_thread = threading.Thread(target=self.nachrichten_empfangen)
            empfang_thread.daemon = True
            empfang_thread.start()
            
            self.nachricht_anzeigen("✅ Erfolgreich verbunden!\n", 'green')
            
        except Exception as e:
            messagebox.showerror("Verbindungsfehler", f"Konnte nicht verbinden:\n{e}")
    
    def nachrichten_empfangen(self):
        """Empfängt Nachrichten vom Server"""
        while self.verbunden:
            try:
                nachricht = self.client.recv(1024).decode('utf-8')
                if nachricht:
                    # Farbcodierung für verschiedene Nachrichtentypen
                    if nachricht.startswith("SERVER:"):
                        self.nachricht_anzeigen(nachricht + "\n", 'blue')
                    elif "PRIVAT" in nachricht:
                        self.nachricht_anzeigen(nachricht + "\n", 'purple')
                    else:
                        self.nachricht_anzeigen(nachricht + "\n", 'black')
                else:
                    break
            except:
                break
    
    def sende_nachricht(self):
        """Sendet Nachricht an Server"""
        nachricht = self.nachricht_entry.get().strip()
        if nachricht and self.verbunden:
            try:
                self.client.send(nachricht.encode('utf-8'))
                self.nachricht_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Fehler", f"Nachricht konnte nicht gesendet werden:\n{e}")
    
    def nachricht_anzeigen(self, nachricht, farbe='black'):
        """Zeigt Nachricht im Chat-Fenster an"""
        self.chat_display.config(state='normal')
        
        # Tag für Farbe erstellen
        tag_name = f"color_{farbe}"
        if farbe == 'blue':
            self.chat_display.tag_config(tag_name, foreground='#3498db', font=('Arial', 10, 'bold'))
        elif farbe == 'green':
            self.chat_display.tag_config(tag_name, foreground='#27ae60', font=('Arial', 10, 'bold'))
        elif farbe == 'purple':
            self.chat_display.tag_config(tag_name, foreground='#9b59b6', font=('Arial', 10, 'italic'))
        else:
            self.chat_display.tag_config(tag_name, foreground='#2c3e50')
        
        self.chat_display.insert(tk.END, nachricht, tag_name)
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def beim_schliessen(self):
        """Wird beim Schließen aufgerufen"""
        if self.verbunden:
            self.client.close()
        self.window.destroy()
    
    def run(self):
        """Startet die GUI"""
        self.window.mainloop()


# ==================== HAUPTPROGRAMM ====================
def main():
    print("=" * 50)
    print("💬 PYTHON CHAT-ANWENDUNG")
    print("=" * 50)
    print()
    print("Wähle eine Option:")
    print("1. Server starten")
    print("2. Client starten (Chat-Fenster)")
    print()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--server':
            wahl = '1'
        elif sys.argv[1] == '--client':
            wahl = '2'
        else:
            wahl = input("Deine Wahl (1 oder 2): ")
    else:
        wahl = input("Deine Wahl (1 oder 2): ")
    
    if wahl == '1':
        server = ChatServer()
        server.start()
        try:
            # Server läuft, bis Ctrl+C gedrückt wird
            input("Drücke ENTER zum Beenden...\n")
        except KeyboardInterrupt:
            pass
        finally:
            print("\n🛑 Server wird beendet...")
            server.stop()
    
    elif wahl == '2':
        client = ChatClient()
        client.run()
    
    else:
        print("❌ Ungültige Auswahl!")


if __name__ == "__main__":
    main()