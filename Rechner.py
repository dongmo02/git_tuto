def principalerechner (nombre):
    # debut de la fonction rechner
    if "(" and ")" in nombre:
        def rechner(nombre):
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
                    listedenombre.remove(0)
                    u = u - 1

                while i <= u:
                    if signe in nombre:
                        Liste.insert(t, nombre[:(listedenombre[c])])
                        nombre = nombre[(listedenombre[c] + 1):]
                    else:
                        Liste.insert(t, nombre)

                    i += 1
                    t += 1
                return Liste

            def Mal(liste):
                a = 1
                for i in liste:
                    i = float(i)
                    a *= i
                return a

            def plus(liste):
                a = 0
                for i in liste:
                    i = float(i)
                    a += i
                return a

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

            if "+" in nombre or ("+" in nombre and "-" in nombre) or (
                    "+" in nombre and "*" in nombre) and "*" not in nombre and "/" not in nombre and "(" not in nombre:
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
                Liste = monspilt("*", nombre)
                resul = Mal(Liste)
                return resul

            elif "/" in nombre and "-" not in nombre and "*" not in nombre and "+" not in nombre:
                Liste = monspilt("*", nombre)
                resul = geteilt(Liste)
                return resul
            else:
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
  # ich kümmere mich hier um die Klammer.
        l1 = []
        l2 = []
        u = 0
        for i in nombre:
            if i == "(":
                l1.insert(u, u)
            if i == ")":
                l2.insert(u, u)
            u = u + 1
        o = 0
        resu = 0
        while "(" and ")" in nombre and o != len(l1):
            a = int(l1[o]) + 1
            b = int(l2[o])
            if "(" and ")" in nombre:
                nombre3 = nombre
                nombre1 = nombre[a:b]
                resu = rechner(nombre1)
                nombre2 = nombre3.replace(nombre[a - 1:b + 1], str(resu))
            o = o + 1

sed.py        nombre = str(nombre2)

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
            listedenombre.remove(0)
            u = u - 1

        while i <= u:
            if signe in nombre:
                Liste.insert(t, nombre[:(listedenombre[c])])
                nombre = nombre[(listedenombre[c] + 1):]
            else:
                Liste.insert(t, nombre)

            i += 1
            t += 1
        return Liste

    def Mal(liste):
        a = 1
        for i in liste:
            i = float(i)
            a *= i
        return a

    def plus(liste):
        a = 0
        for i in liste:
            i = float(i)
            a += i
        return a

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

    def geteilt(liste):
        a = 1
        o = 0
        t = 0
        for i in liste:
            i = float(i)
            if o == 0:
                a = i
                o = 26
                continue
            i = float(i)
            t = a / i

        return t



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

    # ici commence le code principale
    if "(" and ")" not in nombre:
        if "+" in nombre or ("+" in nombre and "-" in nombre) or (
                "+" in nombre and "*" in nombre) and "*" not in nombre and "/" not in nombre and "(" not in nombre:
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
                return resul


        elif "*" in nombre and "-" not in nombre and "+" not in nombre and "/" not in nombre:
            Liste = monspilt("*", nombre)
            resul = Mal(Liste)
            return resul

        elif "/" in nombre and "-" not in nombre and "*" not in nombre and "+" not in nombre:
            Liste = monspilt("/", nombre)
            resul = geteilt(Liste)
            return resul
        else:
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

