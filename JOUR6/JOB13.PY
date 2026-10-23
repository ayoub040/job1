def supprimer_doublons(liste):
    nouvelle_liste = []

    # Parcours de la liste d'origine
    for element in liste:
        # Vérification manuelle si l'élément existe déjà
        deja_present = False
        for x in nouvelle_liste:
            if x == element:
                deja_present = True
                break

        # Si l'élément n'est pas encore présent, on l'ajoute
        if not deja_present:
            nouvelle_liste += [element]

    return nouvelle_liste


# Liste initiale
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Exécution
L_sans_doublons = supprimer_doublons(L)
