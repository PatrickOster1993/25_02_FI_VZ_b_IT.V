import tkinter as tk
root = tk.Tk()
root.title("fensterfenster")
root.geometry("300x300")

label = tk.Label(root, text="Hallo, das ist tkinter!")
label.pack(pady=20)
 
root.mainloop()

