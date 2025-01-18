import os
import tkinter as tk
from tkinter import messagebox

def launch_minecraft():
    try:
        # Otevření Minecraft Bedrock - cesta může být různá dle vaší instalace
        os.system("start minecraft://")  # Spustí Minecraft Bedrock přes protokol
    except Exception as e:
        # Pokud se objeví chyba, zobrazí se zpráva
        messagebox.showerror("Error", f"Failed to launch Minecraft: {str(e)}")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Minecraft Bedrock Launcher")

# Nastavení velikosti okna
root.geometry("300x150")

# Přidání popisku
label = tk.Label(root, text="Click the button to launch Minecraft Bedrock!", wraplength=250, justify="center")
label.pack(pady=20)

# Přidání tlačítka
launch_button = tk.Button(root, text="Launch Minecraft", command=launch_minecraft, bg="green", fg="white")
launch_button.pack(pady=10)

# Spuštění hlavní smyčky aplikace
root.mainloop()
