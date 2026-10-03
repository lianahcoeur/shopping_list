def liste_de_course(liste):
    liste_complete = ""

    for article in liste:
        liste_complete = liste_complete + "[] " + article + "\n"

    print(liste_complete)
    return


liste_souhait = []
liste_souhait.append("mms")
liste_souhait.append("gateau")
liste_souhait.append("champomi")
liste_souhait.append("bonbon")
liste_souhait.append("oignon")
liste_souhait.append("salade")
liste_souhait.append("tomate")
liste_souhait.append("flipper zero")

liste_de_course(liste_souhait)