from tkinter import *
from Rechner  import *
from Ueberblick import *

create()
# Funktion Nummer gibt die Zahl zurück
def nummer(zahl):
    return zahl

# Hauptfenster erstellen
seite = Tk()
seite.title("Rechner")
#seite.geometry("400*400")

# Globale Variable Zahl
global zahl
zahl="0"

# Wenn Zahl gleich 0 ist, Label anzeigen
if  zahl=="0":
    etikett1 = Label(text="0", width=61, height=4, fg="blue", bg="white" ,font=("arial",15,"bold"))
    etikett1.place(x="400", y="110")

# Funktion Alles Löschen
def alles_loeschen():
    global zahl
    etikett1 = Label(text="0", width=61, height=4, fg="blue", bg="white", font=("arial", 15, "bold"))
    etikett1.place(x="400", y="110")
    zahl=""

# Funktion Löschen (ein Zeichen entfernen)
def loeschen():
    global zahl
    a=len(zahl)
    zahl=zahl[:a-1]
    zahl1 = zahl
    le = len(zahl1)
    u = 0
    while le > u:
        if zahl1[u] == "*":
            zahl1 = zahl1.replace("*", "×")
        if zahl1[u] == "/":
            zahl1 = zahl1.replace("/", "÷")
        u += 1
    a=zahl1
    if zahl=="":
        a=0

    etikett = Label(text=a, width=61, height=4, fg="blue", bg="white", font=("arial", 14, "bold"))
    etikett.place(x="400", y="110")

# Funktion Nummer
def nummer(nom):
    global zahl

    if zahl=="0":
        zahl=""
    if nom !="=":
        zahl=zahl+nom
        zahl1=zahl
        le=len(zahl1)
        u=0
        while le>u:
            if zahl1[u]=="*":
                zahl1=zahl1.replace("*","×")
            if zahl1[u]=="/":
                zahl1=zahl1.replace("/","÷")
            u+=1
        etikett = Label(text=zahl1, width=61, height=4, fg="blue", bg="white" ,font=("arial",14,"bold"))
        etikett.pack_propagate(False)
        etikett.place(x="400", y="110")
    else:
        ergebnis=principalerechner(zahl)
        append(str(zahl)+"="+str(ergebnis)+"\n")
        ergebnis=str(ergebnis)

        zahl1 = zahl
        le = len(zahl1)
        u = 0
        while le > u:
            if zahl1[u] == "*":
                zahl1 = zahl1.replace("*", "×")
            if zahl1[u] == "/":
                zahl1 = zahl1.replace("/", "÷")
            u += 1
        etikett = Label(text=zahl1+"                                                            "+ ergebnis, width=61, height=4, fg="blue", bg="white" ,font=("arial",14,"bold"))
        etikett.place(x="400", y="110")
        etikett.pack_propagate(False)

# Hintergrundfarbe setzen
seite['bg']="grey"
rahmen=Frame(seite)
rahmen['bg']="blue"
rahmen.place(x="398" , y="200"  )

# Begrüßungstext
etikett=Label(text="Willkommen in meinem Taschenrechner" ,fg="blue" ,bg="black"  ,font=("arial",0,"bold",  ))
etikett.place(x="0" ,y="0")

inhalt=StringVar
x=25
y=6

etikett.place(x="600" , y="3")

# Tasten erstellen
klammer_auf = Button(rahmen, text="(", bg="black", fg="white", command=lambda:nummer("("), width=x, height=y)
klammer_auf.grid(column=0, row=0)

klammer_zu = Button(rahmen, text=")", bg="black", fg="white", command=lambda:nummer(")"), width=x, height=y)
klammer_zu.grid(column=1, row=0)

loeschen_btn = Button(rahmen, text="←", bg="black", fg="white", command=loeschen, width=x, height=y)
loeschen_btn.grid(column=2, row=0)

geteilt = Button(rahmen, text="÷", bg="black", fg="white", command=lambda:nummer("/"), width=x, height=y)
geteilt.grid(column=3, row=0)

sieben = Button(rahmen, text="7", bg="black", fg="white", command=lambda:nummer("7"), width=x, height=y)
sieben.grid(column=0, row=1)

acht = Button(rahmen, text="8", bg="black", fg="white", command=lambda:nummer("8"),width=x, height=y)
acht.grid(column=1, row=1)

neun = Button(rahmen, text="9", bg="black", fg="white", command=lambda:nummer("9"), width=x, height=y)
neun.grid(column=2, row=1)

mal = Button(rahmen, text="×", bg="black", fg="white", command=lambda:nummer("*"), width=x, height=y)
mal.grid(column=3, row=1)

vier = Button(rahmen, text="4", bg="black", fg="white", command=lambda:nummer("4"), width=x, height=y)
vier.grid(column=0, row=2)

fuenf = Button(rahmen, text="5", bg="black", fg="white", command=lambda:nummer("5"), width=x, height=y)
fuenf.grid(column=1, row=2)

sechs = Button(rahmen, text="6", bg="black", fg="white", command=lambda:nummer("6"), width=x, height=y)
sechs.grid(column=2, row=2)

minus = Button(rahmen, text="-", bg="black", fg="white", command=lambda:nummer("-"), width=x, height=y)
minus.grid(column=3, row=2)

eins = Button(rahmen, text="1", bg="black", fg="white", command=lambda:nummer("1"), width=x, height=y)
eins.grid(column=0, row=3)

zwei = Button(rahmen, text="2", bg="black", fg="white", command=lambda:nummer("2"), width=x, height=y)
zwei.grid(column=1, row=3)

drei = Button(rahmen, text="3", bg="black", fg="white", command=lambda:nummer("3"), width=x, height=y)
drei.grid(column=2, row=3)

plus = Button(rahmen, text="+", bg="black", fg="white", command=lambda:nummer("+"), width=x, height=y)
plus.grid(column=3, row=3)

null = Button(rahmen, text="0", bg="black", fg="white", command=lambda:nummer("0"), width=x, height=y)
null.grid(column=0, row=4)

komma = Button(rahmen, text=".", bg="black", fg="white", command=lambda:nummer("."), width=x, height=y)
komma.grid(column=1, row=4)

alles_loeschen_btn = Button(rahmen, text="AC", bg="black", fg="white", command=alles_loeschen, width=x, height=y)
alles_loeschen_btn.grid(column=2, row=4)

gleich = Button(rahmen, text="=", bg="black", fg="white", command=lambda:nummer("="), width=x, height=y)
gleich.grid(column=3, row=4)

# Hauptschleife starten
seite.mainloop()
