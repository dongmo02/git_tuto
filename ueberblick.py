# erstellung von der funktion überblick

def create():
    file=open("ueberblick.txt","a")
    if(file==None):
        print(" the open's file is failed")

def append(nomber):
    file = open("ueberblick.txt", "a+")
    file.closed
    vorlezte=file.readline()
    file = open("ueberblick.txt", "w")
    file.write(nomber)
    file.writelines(vorlezte)
