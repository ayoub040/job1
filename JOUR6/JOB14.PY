def calculer_longueur(chaine):
    """Calcule la longueur d'un texte ou d'une liste sans len()."""
    compteur = 0
    for _ in chaine:
        compteur += 1
    return compteur


def decouper_texte(texte):
    """Découpe un texte en liste de mots sans split()."""
    mots = []
    mot_actuel = ""
    ponctuations = [" ", ",", ".", ";", ":", "!", "?", "«", "»", "—", "-"]

    for caractere in texte:
        # Vérification si le caractère est un séparateur
        est_separateur = False
        for p in ponctuations:
            if caractere == p:
                est_separateur = True
                break

        if est_separateur:
            if calculer_longueur(mot_actuel) > 0:
                mots += [mot_actuel]
                mot_actuel = ""
        else:
            mot_actuel += caractere

    # Ajout du dernier mot si la chaîne ne se termine pas par une ponctuation
    if calculer_longueur(mot_actuel) > 0:
        mots += [mot_actuel]

    return mots


def my_long_word(n, texte):
    mots = decouper_texte(texte)
    mots_longs = []

    # Filtrage des mots d'une longueur supérieure à n
    for mot in mots:
        if calculer_longueur(mot) > n:
            mots_longs += [mot]

    # Recomposition de la chaîne finale sans join()
    resultat = ""
    premier = True
    for mot in mots_longs:
        if premier:
            resultat += mot
            premier = False
        else:
            resultat += " " + mot

    return resultat


# Exemple d'utilisation :
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(3, phrase)