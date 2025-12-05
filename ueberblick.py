
# zuerst Erstellung der ueberblickdatei
def create():
    file=open("ueberblick.txt","a")
    if(file==None):
        print(" the open's file is failed")
# implementierung der Funktion append , um neue Operation hinzuzufügen
def append(nomber):
    file = open("ueberblick.txt", "r")
    vorlezte = file.readlines()
    file.close()
    file = open("ueberblick.txt", "w")
    file.write(nomber)
    file.writelines(vorlezte)
    file.close()
  # implementierung der funktion Überblick , um den Benutzer , eine Überblick über seine Operationen , zu verschaffen
def ueberblick():
    file = open("ueberblick.txt", "r")
    uberblick = file.readlines()
    return uberblick
