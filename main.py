import tkinter as tk
from PIL import Image, ImageTk  # Requires the Pillow library
import random
import os  # För att kontrollera om filer finns

# Karaktärer och deras namn
karaktarer = [
    {"namn": "Alex", "profil": "Alex gillar att läsa böcker och gå på promenader.", "bild": "images/coolguy.jpg"},
    {"namn": "Sam", "profil": "Sam älskar att laga mat och titta på filmer.", "bild": "images/asianchick.jpg"},
    {"namn": "Jamie", "profil": "Jamie tycker om att resa och spela gitarr.", "bild": "images/zest.jpg"}
]

# Globala variabler
index = 0
val_frame = None
gillade_karaktarer = []  # Lista för karaktärer som gillade dig
bilder = {}  # För att lagra PhotoImage-objekt

# Skapa huvudfönster
root = tk.Tk()
root.title("VDP?")
root.geometry("400x500")

namn_label = tk.Label(root, text="", font=("Helvetica", 16))
namn_label.pack(pady=10)

profil_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350)
profil_label.pack(pady=10)

bild_label = tk.Label(root)
bild_label.pack(pady=10)

svar_label = tk.Label(root, text="", font=("Helvetica", 12))
svar_label.pack(pady=10)

# Ladda bilder
fallback_image = ImageTk.PhotoImage(Image.new("RGB", (200, 200), color="gray"))  # Fallback-bild
for karaktar in karaktarer:
    if os.path.exists(karaktar["bild"]):  # Kontrollera om bildfilen finns
        img = Image.open(karaktar["bild"])
        img = img.resize((200, 200), Image.LANCZOS)  # Ändra storlek på bilden
        bilder[karaktar["namn"]] = ImageTk.PhotoImage(img)
    else:
        bilder[karaktar["namn"]] = fallback_image  # Använd fallback-bild om filen saknas

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
    bild_label.config(image=bilder[person["namn"]])

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
    namn_label.config(text="Finns inga mer personer!")
    profil_label.config(text="")
    bild_label.config(image="")
    if val_frame:
        val_frame.destroy()

    if gillade_karaktarer:
        svar_label.config(text=f"Följande karaktärer gillade dig: {', '.join(gillade_karaktarer)}")
        tk.Button(root, text="Fortsätt prata", command=fortsatt_prata, font=("Helvetica", 14), width=20).pack(pady=20)
    else:
        svar_label.config(text="Ingen karaktär gillade dig. Tack för att du deltog!")

# Funktion: Fortsätt prata
def fortsatt_prata():
    global val_frame
    if val_frame:
        val_frame.destroy()

    namn_label.config(text="Välj en karaktär att prata med:")
    profil_label.config(text="")
    svar_label.config(text="")
    bild_label.config(image="")

    val_frame = tk.Frame(root)
    val_frame.pack()

    for namn in gillade_karaktarer:
        tk.Button(val_frame, text=namn, command=lambda n=namn: prata_med(n), font=("Helvetica", 14), width=20).pack(pady=5)

# Funktion: Prata med en karaktär
def prata_med(namn):
    namn_label.config(text=f"Du pratar med {namn}!")
    profil_label.config(text="")
    svar_label.config(text="Tack för att du fortsätter prata!")
    bild_label.config(image=bilder[namn])

# Visa startmeny
def visa_startmeny():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    namn_label.config(text="Välkommen till 'VDP?'")
    profil_label.config(text="")
    svar_label.config(text="Tryck på knappen för att börja leta!")
    bild_label.config(image="")

    tk.Button(val_frame, text="Börja", command=starta_dejt, font=("Helvetica", 14), width=20).pack(pady=20)

visa_startmeny()

# Starta loopen
root.mainloop()