import tkinter as tk
import random

# Karaktärer och deras namn
karaktarer = [
    {"namn": "Alex", "poang": 0},
    {"namn": "Sam", "poang": 0},
    {"namn": "Jamie", "poang": 0}
]

# Globala variabler
index = 0
val_frame = None

# Skapa huvudfönster
root = tk.Tk()
root.title("Speeddating Simulator")
root.geometry("400x300")

namn_label = tk.Label(root, text="", font=("Helvetica", 16))
namn_label.pack(pady=20)

svar_label = tk.Label(root, text="", font=("Helvetica", 12))
svar_label.pack(pady=10)

# Funktion: Hantera val
def val1():
    karaktarer[index]["poang"] += 1
    svar_label.config(text="Bra val!")

def val2():
    karaktarer[index]["poang"] += 0
    svar_label.config(text="Hmm, inte imponerad...")

def val3():
    karaktarer[index]["poang"] -= 1
    svar_label.config(text="Det föll inte i smaken!")

# Funktion: Visa valknappar
def visa_val():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    tk.Button(val_frame, text="Ge komplimang", command=val1).pack(pady=5)
    tk.Button(val_frame, text="Fråga om väder", command=val2).pack(pady=5)
    tk.Button(val_frame, text="Prata om dig själv", command=val3).pack(pady=5)

# Funktion: Starta dejt
def starta_dejt():
    global index, val_frame
    if val_frame:
        val_frame.destroy()
        svar_label.config(text="")

    if index < len(karaktarer):
        person = karaktarer[index]
        namn_label.config(text=f"Du dejtar {person['namn']}")
        visa_val()
        root.after(8000, byt_dejt)  # 8 sekunder per dejt
    else:
        visa_resultat()

# Funktion: Byt till nästa dejt
def byt_dejt():
    global index
    index += 1
    starta_dejt()

# Funktion: Visa resultat
def visa_resultat():
    namn_label.config(text="Dejtingrundan är över!")
    if val_frame:
        val_frame.destroy()

    # Hitta bästa match
    bast = max(karaktarer, key=lambda p: p["poang"])
    svar_label.config(text=f"Bäst matchade du med {bast['namn']}! ({bast['poang']} poäng)")

# Starta första dejten
starta_dejt()

# Starta loopen
root.mainloop()