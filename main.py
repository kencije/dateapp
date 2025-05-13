import tkinter as tk
import random

# Karaktärer och deras namn
karaktarer = [
    {"namn": "Alex", "profil": "Alex gillar att läsa böcker och gå på promenader."},
    {"namn": "Sam", "profil": "Sam älskar att laga mat och titta på filmer."},
    {"namn": "Jamie", "profil": "Jamie tycker om att resa och spela gitarr."}
]

# Globala variabler
index = 0
val_frame = None
gillade_karaktarer = []  # Lista för karaktärer som gillade dig

# Skapa huvudfönster
root = tk.Tk()
root.title("VDS?")
root.geometry("400x300")

namn_label = tk.Label(root, text="", font=("Helvetica", 16))
namn_label.pack(pady=10)

profil_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350)
profil_label.pack(pady=10)

svar_label = tk.Label(root, text="", font=("Helvetica", 12))
svar_label.pack(pady=10)

# Funktion: Gilla
def gilla():
    karaktarens_svar = random.choice(["gillar dig tillbaka!", "passar dig!"])
    if karaktarens_svar == "gillar dig tillbaka!":
        gillade_karaktarer.append(karaktarer[index]["namn"])
    svar_label.config(text=f"Karaktären {karaktarer[index]['namn']} {karaktarens_svar}")
    byt_dejt()

# Funktion: Passa
def passa():
    karaktarens_svar = random.choice(["gillar dig tillbaka!", "passar dig!"])
    svar_label.config(text=f"Karaktären {karaktarer[index]['namn']} {karaktarens_svar}")
    byt_dejt()

# Funktion: Visa profil
def visa_profil():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    person = karaktarer[index]
    namn_label.config(text=f"Profil: {person['namn']}")
    profil_label.config(text=person["profil"])

    # Skapa större knappar horisontellt
    knapp_frame = tk.Frame(val_frame)
    knapp_frame.pack(pady=10)

    tk.Button(knapp_frame, text="Gilla", command=gilla, font=("Helvetica", 14), width=10).pack(side=tk.LEFT, padx=10)
    tk.Button(knapp_frame, text="Passa", command=passa, font=("Helvetica", 14), width=10).pack(side=tk.LEFT, padx=10)

# Funktion: Starta dejt
def starta_dejt():
    global index, val_frame
    if val_frame:
        val_frame.destroy()
        svar_label.config(text="")

    if index < len(karaktarer):
        visa_profil()
    else:
        visa_resultat()

# Funktion: Byt till nästa dejt
def byt_dejt():
    global index, val_frame
    index += 1
    if val_frame:
        val_frame.destroy()
    starta_dejt()

# Funktion: Visa resultat
def visa_resultat():
    global val_frame
    namn_label.config(text="Det finns inga mer personer kvar")
    profil_label.config(text="")
    if val_frame:
        val_frame.destroy()

    if gillade_karaktarer:
        svar_label.config(text=f"{', '.join(gillade_karaktarer)} Gillade dig tillbaka")
        tk.Button(root, text="Fortsätt prata", command=fortsatt_prata, font=("Helvetica", 14), width=20).pack(pady=20)
    else:
        svar_label.config(text="Inga personer gillade dig")

# Funktion: Fortsätt prata
def fortsatt_prata():
    global val_frame
    if val_frame:
        val_frame.destroy()

    namn_label.config(text="Välj en person att prata med:")
    profil_label.config(text="")
    svar_label.config(text="")

    val_frame = tk.Frame(root)
    val_frame.pack()

    for namn in gillade_karaktarer:
        tk.Button(val_frame, text=namn, command=lambda n=namn: prata_med(n), font=("Helvetica", 14), width=20).pack(pady=5)

# Funktion: Prata med en karaktär
def prata_med(namn):
    namn_label.config(text=f"Du pratar med {namn}!")
    profil_label.config(text="")
    svar_label.config(text="Tack för att du fortsätter prata!")

# Visa startmeny
def visa_startmeny():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    namn_label.config(text="Vill du snacka?")
    profil_label.config(text="")
    svar_label.config(text="Tryck på knappen för att bläddra!")

    tk.Button(val_frame, text="Hitta personer", command=starta_dejt, font=("Helvetica", 14), width=20).pack(pady=20)

visa_startmeny()

# Starta loopen
root.mainloop()