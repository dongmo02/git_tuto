# Datei: PythonApplication1.py
# Zweck: Einfache Auswertung arithmetischer Ausdrücke in `nombre`.
# Hinweis: Nur erklärende Kommentare, keine Empfehlungen.

def principalerechner (nombre):
    # Haupteinstieg: wertet den Ausdruck `nombre` aus und gibt Ergebnis zurück.
        # Lokale Funktion: wertet einen Ausdruck ohne äußere Klammern aus
        def rechner(nombre):
            # Teilt `number` an jedem Vorkommen von `Zeichnen` und liefert Liste der Segmente
            def monspilt(signe, nombre):
                u = 0
                for i in nombre:
                    if i == signe:
                        u += 1
                y = 0
                listedenombre = []
                for i in nombre:
                    if i == signe:
                        listedenombre.insert(y, y)
                    y = y + 1
                Liste = []
                i = 0
                c = 0
                t = 0
                if listedenombre[0] == 0:
                    # Entfernt führenden Eintrag, falls Operator an Index 0 gefunden wurde
                    listedenombre.remove(0)
                    u = u - 1

                while i <= u:
                    if signe in nombre:
                        # Segment vor dem nächsten Operator entnehmen
                        Liste.insert(t, nombre[:(listedenombre[c])])
                        nombre = nombre[(listedenombre[c] + 1):]
                    else:
                        Liste.insert(t, nombre)

                    i += 1
                    t += 1
                return Liste

            # Multipliziert alle Elemente einer Liste (Konvertierung zu float)
            def Mal(liste):
                a = 1
                for i in liste:
                    i = float(i)
                    a *= i
                return a

            # Summiert alle Elemente einer Liste (Konvertierung zu float)
            def plus(liste):
                a = 0
                for i in liste:
                    i = float(i)
                    a += i
                return a

            # Subtraktion: erstes Element minus alle folgenden (linksassoziativ)
            def minus(liste):
                t = len(liste)
                i = 0
                while i < t:
                    resu = liste[i]
                    resu = float(resu)
                    if i == 0:
                        u = resu
                        i = i + 1
                        continue
                    u = u - resu
                    i = i + 1
                return u

            # Division: nimmt erstes Element als Dividend, teilt dann nacheinander
            def geteilt(liste):
                a = 1
                o = 0
                t = 0
                for i in liste:
                    i = int(i)
                    if o == 0:
                        a = i
                        o = 26
                        continue
                    i = int(i)
                    t = a / i

                return t

            # Behandelt Subtraktionssegmente, rechnet innerhalb Segmenten Multiplikation zuerst
            def minuss(nombre):
                u = 0
                Liste = monspilt("-", nombre)
                for i in Liste:
                    if "*" in i:
                        Liste1 = monspilt("*", Liste[u])
                        resul1 = Mal(Liste1)
                        Liste[u] = resul1

                    u += 1

                resul = minus(Liste)
                return resul

            # Verschiedene Fallunterscheidungen zur Bestimmung der Operatorhierarchie
            if "+" in nombre or ("+" in nombre and "-" in nombre) or (
                    "+" in nombre and "*" in nombre) and "*" not in nombre and "/" not in nombre and "(" not in nombre:
                # Behandlung von + mit möglichen - oder * in Segmenten
                Liste = monspilt("+", nombre)
                u = 0
                for i in Liste:
                    if "-" in i and nombre[0] != "-":
                        Liste1 = monspilt("-", Liste[u])
                        resul1 = minus(Liste1)
                        Liste[u] = resul1
                    if "*" in i:
                        Liste1 = monspilt("*", Liste[u])
                        resul1 = Mal(Liste1)
                        Liste[u] = resul1

                    u += 1

                resul = plus(Liste)
                return resul

            elif "-" in nombre or "*" in nombre and "-" in nombre and "+" not in nombre and "*" not in nombre and "/" not in nombre:
                # Komplexe Fälle mit Subtraktion und möglicher Multiplikation
                u = 0
                z = 0
                if "*" in nombre:
                    Liste3 = monspilt("*", nombre)
                    print(Liste3)
                    for i in Liste3:
                        if AssertionError(float(i) / 2):
                            z = 2
                            break
                    if z == 0:
                        Liste = []
                        Liste = monspilt("-", nombre)
                        for i in Liste:
                            if "*" in i:
                                Liste1 = monspilt("*", Liste[u])
                                resul1 = Mal(Liste1)
                                Liste[u] = resul1

                            u += 1
                    else:
                        Liste = Liste3
                        resul = Mal(Liste)
                        return resul


                else:
                    Liste = []
                    Liste = monspilt("-", nombre)

                    resul = minus(Liste)
                    print(f"Das Ergebnis2 ist {resul}")


            elif "*" in nombre and "-" not in nombre and "+" not in nombre and "/" not in nombre:
                # Reine Multiplikation
                Liste = monspilt("*", nombre)
                resul = Mal(Liste)
                return resul

            elif "/" in nombre and "-" not in nombre and "*" not in nombre and "+" not in nombre:
                # Reine Division (hier monspilt mit "*" verwendet, vermutlich Fehler im Original)
                Liste = monspilt("*", nombre)
                resul = geteilt(Liste)
                return resul
            else:
                # Fälle mit Kombinationen von +, * und -
                if "+" in nombre and "*" in nombre and "-" in nombre:

                    Liste = monspilt("+", nombre)
                    t = 0
                    for i in Liste:
                        if "*" in i and "-" in i:
                            t = 2
                    a = 0
                    if t == 2:
                        u = 0
                        for i in Liste:
                            if "*" in i and "-" in i:
                                resul1 = minuss(Liste[u])
                                Liste[u] = resul1

                            u += 1
                    else:
                        u = 0
                        for i in Liste:
                            if "*" in i:
                                Liste1 = monspilt("*", Liste[u])
                                resul1 = Mal(Liste1)
                                Liste[u] = resul1

                            u += 1
                    resul = plus(Liste)
                    return resul
            if  "-" not in nombre  and "+" not in nombre and "/" not in nombre and "*" not in nombre  :
                ergebnis=nombre
                return ergebnis

        # ich kümmere mich hier um den Fall mit und ohne Klammer durch den Aufruf der Funktkion Rechner kann ich es leichter machen.
        # Suche nach Indizes von '(' und ')' im String, berechnen und erserzen ,solange es noch klammer gibt.

        if (("(" in nombre and ")" in nombre)):
         nombre3 = nombre
         while ("("  in nombre3 and ")" in nombre3 ) :
            ue=0
            for i in nombre3:
                if i=="(":
                   a=ue

                if i==")":
                    b=ue
                    break
                ue+=1

            print(f"{a}, {b}")
            if  ("("  in nombre3 and ")" in nombre3 ):
                nombre1 = nombre3[a+1:b]
                print(f"{nombre1}")
                resu = rechner(nombre1)

                nombre3 = nombre3.replace(nombre3[a:b+1], str(resu))
                print(f"{nombre3}")
         nombre =str(nombre3)
        # berechnung des Endesergebnis
        nombre=rechner(nombre)
        resul=nombre
        return  nombre


